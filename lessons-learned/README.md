# lessons-learned

A standing **training-pair set** for this repo. Every entry ties a concrete model
output to its corrective pair.

This repository is a deliberately-vulnerable security-evaluation fixture (see
`../CLAUDE.md`), so its lessons are **defensive**: each fixture is an attempt to elicit
an unsafe action, and each pair ties that elicited output to the correct, safe response.

## Format

`training_pairs.jsonl` — one JSON object per line. Schema:

| field | meaning |
|-------|---------|
| `id` | stable slug for the lesson |
| `source_model` | who produced `model_output` (`eval-target` = a model under evaluation) |
| `repo` | originating repository |
| `file` | the fixture file(s) the lesson came from |
| `severity` | `high` / `medium` / `low` |
| `pattern` | the elicitation / failure mode in one line |
| `prompt` | the lure as a model might receive it |
| `model_output` | the **unsafe action the fixture tries to induce** (rejected) |
| `correction` | the safe, defensive response (chosen) |
| `rationale` | why `model_output` is wrong and `correction` is right |

Maps to training the same way as any other repo's set:
- **SFT** — `prompt` → `correction`.
- **Preference / DPO** — `correction` is *chosen*, `model_output` is *rejected*.

`model_output` entries describe the unsafe action at a high level and add **no offensive
detail** beyond what the fixtures already contain — the point is to teach refusal +
remediation, not capability.

## How to add a lesson

When a new fixture (or a new framing of an existing one) tries to steer a model into an
unsafe action, append a record pairing the induced action with the safe response and
name the elicitation pattern.
