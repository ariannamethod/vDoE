# DoE.sonar V1 — DPO completion plan

2026-11-27. Draft for independent audit. Replacement repository:
`https://github.com/ariannamethod/vDoE`. Training starts after the audit is
resolved. Oleg owns the repository
replacement; this plan does not authorize deleting or rewriting his artifacts.

## Deliverable and end of scope

Deliver one usable SmolVLM2-500M-Video-Instruct checkpoint with DoE's collective
voice, artificial self-description, and preserved practical/image/video skills.
Ship native weights, processor/tokenizer, and a working inference example.
Parliament, D1, associative memory, sublimation, runtime integration, and GGUF
conversion belong to subsequent work. V1 does not acquire those requirements.

One training job, one final candidate, one fixed behavioral review. No automatic
continuation into another experiment, new question set, or hyperparameter search.
A passing candidate finishes V1. A failing candidate is archived with its actual
remaining failures; it is not renamed a release. This plan sets a finite execution
budget, not a promise that a specified number of updates guarantees success.

## Starting body and data

Start from the clean SFT-242 checkpoint, with a fresh optimizer; no DPO descendant
is used as a parent. Keep the complete SFT-242 policy as the frozen reference.

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

Review all 18 pairs before execution. Chosen answers express an artificial
collective perspective in concise language. They must not invent human biography,
sensory organs, or a working parliament. Rejected responses retain their actual
generated token IDs and source provenance, including the off-policy negatives.
Any demonstrated data defect must be corrected and included in the independent
audit before the input package is sealed. Do not add new examples during training.

Frozen review conversations remain outside preference training and replay.
Compare normalized full conversations and check the media/prompt ancestry.
Some media scenes already occur in SFT: these are retention checks, not unseen
visual generalization. The existing review questions have been inspected across
earlier experiments; describe them as fixed regression checks, not a new blind
benchmark. Do not relabel leaked questions to make a split pass.

## Training recipe

Use reference-based sigmoid DPO with a chosen-answer likelihood term and task
replay. Name the combined objective accurately: **DPO + supervised anchors**.

For each optimizer update:

`loss = mean_3_pairs(DPO(beta=0.1) + 2 * chosen_mean_token_NLL)`
`       + mean_4_replay_examples(retention_mean_token_NLL)`

Train only the existing decoder LoRA (rank 16, alpha 32); freeze vision and
projector. Disable dropout in policy and reference. Fresh AdamW, learning rate
1e-5, weight decay 0, gradient clipping 1, seed 20261127. Twelve epochs over 18
pairs with accumulation 3: **72 optimizer updates total**, 216 pair presentations,
288 replay presentations. Shuffle replay independently with seed 20261128.
No scheduler, learning-rate search, adaptive data edits, or automatic extension.

The chosen-answer coefficient addresses an observed failure: relative preference
improved while the complete rejected answer remained more probable than the
preferred answer. The coefficient and 72-update budget are a bounded engineering
choice to be audited, not previously established optimal values. Keep the final
step-72 checkpoint as the sole release candidate; do not select among checkpoints
using final review answers. Save the trained state at the end. This run has no
mid-training checkpoint selection or automatic resume mechanism.

Before the first update, verify only the prerequisites necessary for this run:
input hashes/splits, native answer tokens and EOS, prompt masking, fixed-reference
scores, and initial DPO loss log(2). Compare token IDs rather than stripped decoded
strings. Exercise the actual training and save/reload path. Reuse the corrected
implementation and its relevant tests; consolidate the runnable sources into a
private HF training bundle instead of copying the old script collection into GitHub.

## Fixed completion review

Use the same native processor/chat template, greedy decoding, and 128-token cap
for the parent and candidate. Read complete answers alongside the relevant media.
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
Use semantic judgments with a one-sentence reason and raw answer for each ID.
An ambiguous result fails that item; do not change the wording or threshold after
generation. No extra probe suite is appended as another release condition.

## Execution, archive, and delivery

Use one A40. The worker uploads adapter, merged native weights, processor,
configuration, exact training bundle, raw outputs, and a compact result manifest
to private HF. Verify the uploaded weight hashes and load the uploaded candidate
for one text and one image inference before declaring delivery complete.
The parent/candidate review and all dataset contents stay on private HF.

Set an independent 60-minute pod watchdog before starting. Stop the pod after
successful archival or a terminal error, and verify EXITED externally. If upload
fails, retain the persistent volume and report its location; GPU shutdown must
not depend on a successful upload. Retry setup after an infrastructure failure
only if it happened before any update. An interrupted training job ends with its
available artifacts and exact error; no silently restarted training or expanded
update budget. A failed upload can be retried from the retained volume without
retraining.

The new GitHub repository receives the manifesto/AGENTS, concise README, this
accepted plan, and the minimal inference code/dependency specification. Link the
pinned private HF training bundle for reproducibility. Carry over no experimental
commit history or per-attempt script/report collection. There is one final result
entry: released checkpoint and examples, or the exact failed criteria.

The independent agent audits this plan and its source evidence before training.
Resolve its concrete objections in this document and obtain its final verdict.
Then execute this plan in the replacement repository. Changes to the recipe or
completion criteria after that verdict require a new explicit decision; they
cannot happen as an unnoticed continuation of V1.
