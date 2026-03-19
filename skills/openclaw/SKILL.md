---
name: auto-skill-improver-openclaw
description: "OpenClaw-native workflow for improving skills through operational benchmarks, one-change mutation loops, and honest keep/discard decisions."
metadata:
  openclaw:
    emoji: "🧪"
---

# Auto Skill Improver (OpenClaw-native)

This workflow improves SKILL.md files only when the improvement can be grounded in operational behavior.

## Core rule
Do not optimize skill prose directly.
Optimize the behavior the skill induces.

## Inputs required before starting
1. exact path to target `SKILL.md`
2. working directory for artifacts
3. 3-7 representative test prompts
4. 3-6 binary evals tied to operational behavior
5. runs per experiment
6. stopping rules
7. candidate filename for mutated versions

## Skill-type classification
Classify the target before building the harness:
- execution
- routing
- artifact
- formatting/content
- research/audit
- meta-skill

## Baseline-first protocol
1. copy the original skill into a safe candidate
2. keep `SKILL.md.baseline` untouched
3. run the harness on baseline first
4. record total score, per-eval pass counts, and failure cases

## Saturation check
If baseline is already very high, tighten the benchmark before mutating.
If saturation persists, conclude honestly that the skill is already good relative to the benchmark.

## Mutation rules
Change one thing at a time.
Good mutations:
- reorder a priority instruction
- replace vague text with a concrete rule
- add one fallback rule
- add one anti-pattern for a recurring failure
- add one example tied to a failing case
- remove one conflicting or noisy instruction

## Keep/discard rule
- higher score -> keep
- same score -> discard unless materially simpler
- lower score -> discard

## Held-out validation
Use held-out prompts for non-trivial skills. If a mutation improves train prompts but regresses on held-out prompts, discard it.

## Required artifacts
Produce:
- mutated candidate skill(s)
- `SKILL.md.baseline`
- `results.tsv`
- `results.json`
- `changelog.md`
- evaluator or harness scripts
- optional dashboard

## Stopping rules
Stop when:
- budget cap is reached
- no measurable improvement appears after repeated attempts
- score is high and held-out prompts are stable
- the benchmark saturates persistently
- the skill cannot be operationalized honestly

## Philosophy
The harness is the product.
A dashboard is optional.
