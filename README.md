# Auto Skill Improver

Auto Skill Improver is a benchmark-first workflow for improving agent skills through controlled mutation, binary evaluation, and honest keep/discard decisions.

It is designed for people who have real skill files or prompt specs and want to improve them **without lying to themselves** about whether anything actually got better.

## Why this exists

A lot of prompt and skill iteration feels productive while producing no real measurable gain. The common failure mode is simple: people mutate instructions, read the new version, and convince themselves it is stronger because it sounds more sophisticated.

Auto Skill Improver tries to resist that trap.

The core idea is:

1. classify the skill type
2. build a benchmark that can actually distinguish success from failure
3. establish a baseline
4. change one thing at a time
5. keep only what improves the score
6. stop when the benchmark saturates or stops teaching you anything

## Inspiration and credit

This project is directly inspired by **Andrej Karpathy's autoresearch** work.

The important idea we borrowed is not just "let an AI improve itself." It is the much more disciplined principle underneath it:

- use a **bounded environment**
- use a **real benchmark**
- use a **repeatable loop**
- compare against a **baseline**
- make **keep/discard** decisions based on evidence, not vibes

Karpathy's work is compelling because it treats autonomous iteration as an empirical process rather than a magical one. That principle carries over well to skills and prompt specs — but only if you preserve the measurement discipline.

## What this is good for

Auto Skill Improver works best on skills with:

- ambiguous output contracts
- missing fallback behavior
- conflicts between multiple instruction layers
- dependency or portability problems
- research/audit outputs that need stronger evidence discipline
- formatting/content rules that can be checked structurally

Examples:

- a writing skill that needs explicit mode switching
- an audit skill that invents certainty when data is missing
- a multi-skill system with conflicting rules
- a spec that breaks when reference files are unavailable

## What this is **not** good for

This is **not** a universal prompt-optimization machine.

It is a poor fit when:

- the skill is tiny, crisp, and already adequate
- the only thing you care about is subjective taste
- you cannot build a meaningful benchmark
- the benchmark saturates immediately and tightening still does not help
- the target is a high-risk orchestration layer without proxy metrics

## Expectations

Be realistic.

Auto Skill Improver can help you find:
- missing decision logic
- broken dependencies
- contradictory instructions
- weak output contracts
- evaluator saturation

It cannot magically solve:
- taste
- deep product judgment
- audience resonance
- real-world performance without real-world testing

For many formatting/content skills, scores are **directional**, not absolute.

## Core principles

### 1. The harness is the product
A nice dashboard is optional. A benchmark that actually distinguishes good from bad behavior is not.

### 2. Binary evals help, but only if they matter
A binary eval can still be useless. The goal is not just yes/no questions. The goal is yes/no questions tied to task success.

### 3. Baseline first
If you mutate before measuring the starting point, you are doing theater, not research.

### 4. One change at a time
If you change five things at once, you lose attribution.

### 5. Saturation is a finding
If the baseline already scores near-perfectly, that may mean the skill is already good — or your benchmark is weak. Either way, do not pretend you improved something.

### 6. Stop early when the benchmark stops teaching you anything
Longer loops are not always better loops.

## Package contents

- `skills/` — optimizer specs for different execution environments
- `docs/` — limitations, triage, eval patterns, usage guidance
- `harnesses/` — public-safe template harnesses
- `examples/` — synthetic worked examples

## Recommended workflow

1. Read `docs/TRIAGE.md`
2. Pick a target skill
3. Classify the skill type
4. Build a small benchmark
5. Run a baseline
6. Tighten the benchmark if it saturates
7. Mutate one thing
8. Re-run and review the diff
9. Keep or discard honestly

## Use cases

### Good use case: broken dependency
A skill relies on a reference file to perform its core quality check. If the file is missing, the skill's main promise collapses. A fallback mutation can produce a real improvement.

### Good use case: conflicting rule layers
One skill says "close with a statement" while another encourages question endings. Adding an explicit priority rule can be a real, testable improvement.

### Weak use case: tiny command reference
A compact reference skill that already lists the necessary commands may saturate the benchmark immediately. In that case the right answer is often to stop.

## Limitations

This project is deliberately upfront about its limits.

- same-model evaluation can be circular
- formatting/content quality is difficult to measure honestly with binary checks alone
- some skills require proxy benchmarks rather than direct scoring
- portability improvements can conflict with platform-specific optimization

Read `docs/LIMITATIONS.md` before treating any score as definitive.

## Philosophy

The point is not to make skills longer.
The point is to make them **clearer, more robust, and more measurably useful**.

If the benchmark says nothing improved, that is still useful information.

## License

MIT
 robust, and more measurably useful**.

If the benchmark says nothing improved, that is still useful information.

## License

Add your preferred license here.
