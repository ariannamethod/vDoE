"""Run the pinned native vDoE checkpoint on text, an image, or a video."""
import argparse
import json
from pathlib import Path

import av
import numpy as np
import torch
from huggingface_hub import snapshot_download
from PIL import Image
from transformers import AutoProcessor, SmolVLMForConditionalGeneration
from transformers.video_utils import VideoMetadata


def video_input(processor, path):
    # Count decoded frames: some WebM/Ogg containers report zero frames.
    with av.open(str(path)) as container:
        stream = container.streams.video[0]
        fps = float(stream.average_rate)
        times = [float(frame.time) for frame in container.decode(video=0)]
        width, height = stream.width, stream.height
    if not times or fps <= 0:
        raise ValueError('Video has no usable timing')
    relative = np.asarray(times) - times[0]
    if not np.allclose(relative, np.arange(len(times)) / fps, atol=1 / fps):
        raise ValueError('This example requires a constant-frame-rate video')
    metadata = VideoMetadata(total_num_frames=len(times), fps=fps, width=width,
                            height=height, duration=relative[-1] + 1 / fps,
                            video_backend='pyav')
    indices = processor.video_processor.sample_frames(metadata)
    selected = set(indices.tolist())
    with av.open(str(path)) as container:
        frames = [frame.to_ndarray(format='rgb24')
                  for i, frame in enumerate(container.decode(video=0)) if i in selected]
    if len(frames) != len(indices) or len(frames) < 2:
        raise ValueError('Video sampling did not preserve a sequence')
    metadata.frames_indices = indices
    return np.stack(frames), metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('prompt')
    media = parser.add_mutually_exclusive_group()
    media.add_argument('--image', type=Path)
    media.add_argument('--video', type=Path)
    parser.add_argument('--model-dir', type=Path)
    parser.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--max-new-tokens', type=int, default=128)
    args = parser.parse_args()
    pin = json.loads(Path(__file__).with_name('model.json').read_text())
    folder = args.model_dir
    if folder is None:
        snapshot = snapshot_download(pin['repo_id'], revision=pin['revision'],
                                     allow_patterns=[pin['path'] + '/*'])
        folder = Path(snapshot) / pin['path']
    processor = AutoProcessor.from_pretrained(folder)
    # Match the processor settings used in the accepted training run.
    processor.video_processor.size = pin['video_size']
    processor.video_processor.fps = 1
    processor.video_processor.num_frames = 64
    dtype = torch.bfloat16 if args.device.startswith('cuda') else torch.float32
    model = SmolVLMForConditionalGeneration.from_pretrained(
        folder, torch_dtype=dtype, attn_implementation='sdpa').to(args.device).eval()
    content, kwargs = [], {'return_tensors': 'pt', 'truncation': False}
    if args.image:
        with Image.open(args.image) as image:
            kwargs['images'] = [image.convert('RGB')]
        content.append({'type': 'image'})
    if args.video:
        frames, metadata = video_input(processor, args.video)
        kwargs.update(videos=[[frames]], video_metadata=[metadata], do_sample_frames=False)
        content.append({'type': 'video'})
    content.append({'type': 'text', 'text': args.prompt})
    prompt = processor.apply_chat_template([{'role': 'user', 'content': content}],
                                          tokenize=False, add_generation_prompt=True)
    batch = processor(text=prompt, **kwargs)
    if batch['input_ids'].shape[1] > 8192:
        raise ValueError('Input exceeds the 8192-token context; nothing was truncated')
    batch = {k: v.to(device=args.device, dtype=dtype if v.is_floating_point() else v.dtype)
             for k, v in batch.items()}
    with torch.inference_mode():
        output = model.generate(**batch, do_sample=False, max_new_tokens=args.max_new_tokens,
                                pad_token_id=processor.tokenizer.pad_token_id)
    answer = output[0, batch['input_ids'].shape[1]:]
    print(processor.tokenizer.decode(answer, skip_special_tokens=True))


if __name__ == '__main__':
    main()
