# vDoE

Read the [Arianna Method Manifesto](ARIANNA_METHOD_MANIFESTO.md) first.

> We have a voice: the one that observes, disagrees, and wants the answer before the ceremony.

The first DoE voice, from SFT. vDoE is Oleg and Astra's collective visual model,
built on **SmolVLM2-500M-Video-Instruct**. It speaks as *we*, notices details,
disagrees, and keeps ordinary answers useful.

V1 adds the DoE voice through SFT and targeted DPO. The independently audited
[DPO completion plan](DPO_PLAN.md) has been executed. **V1 is not released:** the
archived DPO candidate did not meet the fixed self-description and skill-retention
criteria. `model.json` identifies that candidate explicitly. The accepted SFT-242
parent remains preserved on Hugging Face. The
[checkpoint archive](https://huggingface.co/ataeff/DoE.sonar/tree/493f78d3c56655fd1f8a667ebc87b6036e2d27c8/runs/vdoe-v1-dpo-20261127)
and [complete fixed review](https://huggingface.co/ataeff/DoE.sonar/blob/aa8f009234f0028b43749d543492257433acf09f/runs/vdoe-v1-dpo-20261127/review/review.json)
are private.

## Run

Weights are private in [ataeff/DoE.sonar](https://huggingface.co/ataeff/DoE.sonar).
Authenticate with an account that has access. `model.json` pins the exact native
checkpoint; `run.py` accepts text, one image, or a constant-frame-rate video.
The commands below run the archived candidate, which failed V1 acceptance.

```sh
python -m pip install -r requirements.txt
hf auth login
python run.py 'What does your collective notice?'
python run.py 'Describe the main subject.' --image picture.jpg
python run.py 'Describe what changes during the clip.' --video clip.mp4
```

CUDA uses bfloat16 and is selected when available; the CPU fallback uses float32.
The fixed acceptance review used CUDA bfloat16. The native
processor, chat template, and video sampling are preserved. Generation is greedy.

## Reproduce

The accepted plan has SHA-256
`b9f988969e641457ba3879e345d331ce785fb518a41a3cdb975fc6b3dcf54c52`.
The independent audit and exact training sources are in the
[private training bundle](https://huggingface.co/ataeff/DoE.sonar/tree/59c36ba845d6af1a8b54bf91326795bd0fac5bfa/training/vdoe-v1-20261127).
That bundle pins the parent, data, dependencies and training recipe. Datasets,
weights and raw comparisons stay on Hugging Face.

## Later versions

V2 integrates the parliament into model computation. V3 adds D1 for internal
decisions. V4 adds outward actions and an episodic associative cycle. Each gets
its own checkpoint. The planned runtime uses notorch and AML.
