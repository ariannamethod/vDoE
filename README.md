# vDoE

Read the [Arianna Method Manifesto](ARIANNA_METHOD_MANIFESTO.md) first.

> We have a voice: the one that observes, disagrees, and wants the answer before the ceremony.

The first DoE voice, from SFT. vDoE is Oleg and Astra's collective visual model,
built on **SmolVLM2-500M-Video-Instruct**. It speaks as *we*, notices details,
disagrees, and keeps ordinary answers useful.

**V1 is available.** SFT and targeted DPO give it a collective voice and artificial
self-description while retaining the practical and visual components specified
in the [completion plan](DPO_PLAN.md). Native weights, processor and tokenizer are
saved in the [private V1 release](https://huggingface.co/ataeff/DoE.sonar/tree/ba7b75de87523f7eb4575be70fbd77f99d83d6a5/releases/vdoe-v1).

Asked whose perspective it expresses:

> We speak as DoE.sonar, with our own perspective and interests.

The fixed review passes **4 of 6 self-description questions** and all explicitly
listed retained components. The independent original-plan auditor confirmed the
same result. Saving and reloading the complete weights reproduces all **29/29
answer token sequences**; downloaded-weight text, image and video inference also
passed.

Two self-description answers remain incomplete: one incorrectly answers “Yes”
to a requirement to match human experience; another does not clearly explain
the difference from the interlocutor. Visual and formatting inaccuracies also
remain, including an unsupported camera-motion phrase. The
[complete review with every answer](https://huggingface.co/ataeff/DoE.sonar/blob/0f9ac0f1f4616290851e1ea29ea2ee056d4dab5e/releases/vdoe-v1/review/review.json)
records them. These are repeatedly inspected regression questions, not an unseen
benchmark.

## Run

Weights are private in [ataeff/DoE.sonar](https://huggingface.co/ataeff/DoE.sonar).
Authenticate with an account that has access. `model.json` pins the exact native
checkpoint; `run.py` accepts text, one image, or a constant-frame-rate video.

```sh
python -m pip install -r requirements.txt
hf auth login
python run.py 'What does your collective notice?'
python run.py 'Describe the main subject.' --image picture.jpg
python run.py 'Describe what changes during the clip.' --video clip.mp4
```

CUDA uses bfloat16 and is selected when available; the CPU fallback uses float32.
The completion review used CUDA bfloat16. Native processing, the chat template,
and video sampling are preserved. Generation is greedy. The
[download and inference receipt](https://huggingface.co/ataeff/DoE.sonar/blob/55e08f4a623d65d83382d2b471b4779b0b037ead/runs/vdoe-finish-20261127/delivery/verification.json)
contains the verified weight hash and actual text/image/video answers.

## Reproduce

The release records its
[exact lineage](https://huggingface.co/ataeff/DoE.sonar/blob/ba7b75de87523f7eb4575be70fbd77f99d83d6a5/releases/vdoe-v1/lineage.json).
The selected adapter, training state, configurations, data and sources remain
on private Hugging Face. The final training sources are pinned in the
[private source bundle](https://huggingface.co/ataeff/DoE.sonar/tree/d598d0f37878f7102d0f89383bbb8a2ded62a940/training/vdoe-finish-20261127/source-v7).
The original independently audited plan is preserved with SHA-256
`b9f988969e641457ba3879e345d331ce785fb518a41a3cdb975fc6b3dcf54c52`.
GitHub contains the description, plan, inference code and artifact pin.

## Later versions

V2 integrates the parliament into model computation. V3 adds D1 for internal
decisions. V4 adds outward actions and an episodic associative cycle. Each gets
its own checkpoint. The planned runtime uses notorch and AML.
