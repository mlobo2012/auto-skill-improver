# Run Modes

## 1. Supervised batch mode (recommended default)
Use when:
- you are testing a skill for the first time
- the benchmark is still maturing
- the skill is important but not yet stable

Typical flow:
- baseline
- 1-3 mutations
- held-out check
- summary
- human decision

## 2. Semi-autonomous mode
Use when:
- the benchmark is strong
- stop conditions are explicit
- you trust the mutation scope

Typical stop conditions:
- budget cap reached
- no improvement after N tries
- score is high and held-out prompts are stable
- benchmark saturation persists

## 3. Event-driven rerun mode
This is often the best operational model.
Re-run the optimizer when:
- the skill changes
- the model changes
- the environment changes
- repeated failures show up in practice
- a dependency or portability issue appears

## 4. Periodic review mode
Use sparingly.
Good candidates:
- high-value skills
- heavily used skills
- skills that tend to drift as models improve

Avoid blind timer-based optimization for everything.

## Recommended intervals
- after major model upgrades
- after important skill revisions
- after repeated failure reports
- occasionally for a small set of high-leverage skills
