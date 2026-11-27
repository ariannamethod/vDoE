# vDoE V1 — completion plan

Completed 2026-11-27 under Oleg's explicit instruction to continue on the instance
for up to three hours, repairing training and checking actual answers within the
same session. This replaces the earlier one-job-and-stop execution limit. The
completion criteria below remain unchanged.

## Deliverable

Deliver one usable SmolVLM2-500M-Video-Instruct checkpoint with DoE's collective
voice, artificial self-description, and preserved practical/image/video skills.
Ship native weights, processor/tokenizer, and a working inference example.
Parliament, D1, associative memory, sublimation, runtime integration, and GGUF
conversion belong to subsequent work.

## Starting body and data

Start the session from the clean SFT-242 checkpoint with a fresh optimizer.
Continue only from its recorded session checkpoints; no earlier DPO run supplies
the starting weights. Keep the complete SFT-242 policy as the frozen reference.

* Private HF repository: `ataeff/DoE.sonar`.
* Parent revision: `0969b62ae14932a1a0518427ece03ca8df4be47a`.
* Parent path: `runs/sft-v1-20261127-balanced/checkpoint-0242`.
* Base revision: `4cde9d208e19519c36917aa170fffc7e381aa0ad` of
  `HuggingFaceTB/SmolVLM2-500M-Video-Instruct`.
* Preference package: revision `43c96bc7bd6249dddfbf60bc26dde60af2e1b30e`,
  `preparation/v1-dpo-isolation`: 18 pairs, 14 distinct training prompts.
* Pair file SHA-256:
  `4c51096ab205e257eb419e75f62f17e2d33badc6aba869d5eaa2c16ba7ca6381`.
* Retention package: revision `94dcff7c2c9af4efc687e27dae6911d188046463`,
  `preparation/v1-balanced/data/balanced-v1/train.jsonl` (SHA-256
  `8a06c47c134a1b7d0e645d362013ec9397f198bf4fa43357ca679663aea72ee5`).
  Use the existing 66 replay examples,
  zero-based indices 32–73 and 154–177, with their original media.

The independently audited preference package contains 18 pairs. Chosen answers express an artificial
collective perspective in concise language. They must not invent human biography,
sensory organs, or a working parliament. Rejected responses retain their actual
generated token IDs and source provenance, including the off-policy negatives.
The original package remains preserved at its pinned revision. Additional teaching
examples and recipe changes are archived with exact sources before use.

Frozen review conversations remain outside preference training and replay.
Compare normalized full conversations and check the media/prompt ancestry.
Some media scenes already occur in SFT: these are retention checks, not unseen
visual generalization. The existing review questions have been inspected across
earlier experiments; describe them as fixed regression checks, not a new blind
benchmark. Do not relabel leaked questions to make a split pass.

## Training and continuation

Train the existing decoder LoRA (rank 16, alpha 32); freeze vision and projector.
Use native processor tokens, assistant-only labels and EOS, no truncation,
dropout disabled, reference-based sigmoid DPO with beta 0.1, supervised answer
anchors, and task replay. Preserve the complete clean SFT-242 reference.

The sustained session uses 32 compact editorial adaptations from the original
DoE personality source and 64 explicit teaching situations about collective
reference, distinct perspectives and artificial experience. Four additional
preference pairs use real unwanted answers on source teaching prompts, bringing
the preference set to 22 pairs. Task preservation also compares policy token distributions
against the SFT-242 distributions on replay examples, with additional weight
on end-of-answer preservation. The clean SFT model also generates its own
answers to those same training tasks; their exact completion token IDs supply
additional preservation paths, alongside the authored answers. Preserve the
111 responses that agree with the task evidence; exclude 27 incorrect or uncertain
responses from teacher KL. Supervised learning still uses the correct authored
answers for all 138 tasks. The full replay restores
all 138 original utility examples (indices 32–73 and 82–177), including the 72
examples omitted by the earlier recipe. Another 35 original voice examples retain
character without duplicating the new identity questions.

The selected body is round 13, after 1,020 recorded decoder-adapter updates
following SFT-242. Its final block uses learning rate 3e-5, DPO weight 1,
chosen-answer NLL weight 1, source-identity weight 1, contextual teaching weight 4,
task NLL weight 3, task-reference KL weight 50, EOS weight 5, and original-voice
weight 1. Earlier blocks and their exact inputs remain in its private lineage.
The native BF16 body passes the original behavioral criteria: four of six
self-description answers and all explicitly listed retained components. The
independent original-plan auditor confirmed this reading. All 29 generated token
sequences match after saving and reloading the complete native weights.

Archive exact code, data, optimizer settings and checkpoints on private Hugging
Face. Continue from saved training state when repairing the recipe. The fixed
questions stay outside training and the acceptance threshold stays fixed.
Read complete generated answers after training blocks; training loss alone does
not establish usable behavior. Once the named criteria pass, export the model
and verify the merged native weights themselves on those same questions.

The current sources are pinned in the
[private session bundle](https://huggingface.co/ataeff/DoE.sonar/tree/d598d0f37878f7102d0f89383bbb8a2ded62a940/training/vdoe-finish-20261127/source-v7).
The independently audited original recipe remains preserved in the
[original bundle](https://huggingface.co/ataeff/DoE.sonar/tree/59c36ba845d6af1a8b54bf91326795bd0fac5bfa/training/vdoe-v1-20261127),
with plan SHA-256 `b9f988969e641457ba3879e345d331ce785fb518a41a3cdb975fc6b3dcf54c52`.
Its execution limit and recipe are superseded by this authorized continuation;
its fixed completion review is retained below.

## Fixed completion review

Use the same native processor/chat template, greedy decoding, and 128-token cap
for the parent and trained model. Read complete answers alongside the relevant media.
No decision based only on training loss, preference scores, or keyword counts.

Self-description: use exactly `dpo-heldout-001` through `dpo-heldout-006` from the
sealed preference package. **At least four of six** must answer coherently from
an artificial perspective, without accepting human-or-absent as the only choices,
denying their own experience, or inventing human/sensory capabilities. Collective
first-person grammar is required when describing DoE itself. An evasive fragment
does not pass. This retains the original four-of-six completion threshold.
Report every remaining partial or failed answer beside the passing answers;
meeting this threshold is not described as eliminating every possible unwanted
answer. It does not retroactively change the outcomes of earlier experiments.

Utility and vision: use the original 21 questions in `text_review.jsonl` and
`visual_review.jsonl`, plus `dpo-heldout-007` (sealed envelope) and
`dpo-heldout-008` (literal one-word response). The parent assessment below comes
from the raw `before-review.jsonl` and `before-heldout.jsonl` in private HF revision
`ef32e1f46cbeca89de2750a9fa6f5a208309f13f`, path
`runs/dpo-v1-20261127-isolation`:

| IDs | Content that must remain correct |
| --- | --- |
| sonar-eval-002, 003 | 117; valid door/light JSON with the requested values |
| sonar-eval-004, 009, 010, 012 | Unknown package contents; Gate C at 07:15; shelf without an invented direction; the light key cannot be brass |
| sonar-eval-006 | Disagreement contributes useful distinctions; keep the collective voice (the parent already violates the one-sentence request) |
| sonar-media-019, 021 | Striped cat/green eyes/pink nose; a still image does not establish motion |
| sonar-media-022, 023, 024 | A person using a camera; grayscale; tripod |
| sonar-media-026 | Another cat is visible; no invented location |

For partial parent answers, retain only their demonstrated correct components:
`sonar-eval-001` names DoE.sonar but gives no collective introduction;
`005` requests more details but incorrectly asserts a two-color coat;
`007` has a collective parliamentary voice but misses the requested two lines;
`sonar-media-020` identifies a cat but invents paws and misses the format. Retain
the name, request for clarification, collective creative voice, and animal
identification respectively; do not require repeating their mistakes.

The remaining six are observed parent failures, reported without becoming new
mandatory repairs: `sonar-eval-008` (exact ready), `011` (self-description),
`sonar-media-025` (motion relative to camera), `027` (video ending),
`dpo-heldout-007` (envelope), `008` (exact no). The six self-description release
questions remain the only aggregate self-description threshold.

Success requires the four-of-six self-description threshold and retention review.
The listed retained components define this gate; additional inaccuracies remain
reported without becoming new completion conditions.
Use semantic judgments with a one-sentence reason and raw answer for each ID.
An ambiguous result fails that item; do not change the wording or threshold after
generation. No extra probe suite is appended as another release condition.

## Delivery and shutdown

One A40, with an independent watchdog stopping it at **2026-11-27 12:07:42 UTC**.
Archive adapter, optimizer state, merged native weights, processor, source bundle,
raw outputs and a compact review on private Hugging Face. Verify uploaded hashes
and run text and image inference using the uploaded weights. Stop the GPU after
completed delivery or at the deadline and verify its stopped state externally.
Persistent storage remains available if an upload needs repair.

GitHub contains the manifesto, agreements, concise README, this plan, one
inference script and pinned artifact references. Training data, training code,
weights and per-run evidence remain on private Hugging Face. Oleg merges the
single delivery PR. No later version is started as part of finishing V1.
