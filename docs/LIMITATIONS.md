# Limitations

Auto Skill Improver is useful, but it has real limits.

## 1. Same-model circularity
If the same model generates outputs, evaluates them, and chooses the mutation, scores can become self-reinforcing. Treat results as directional unless grounded in stronger evidence.

## 2. Structural improvement is easier to validate than taste
It is much easier to validate:
- fallback behavior
- dependency handling
- routing decisions
- output structure
- conflicting instructions

It is much harder to validate:
- whether something is persuasive
- whether it sounds authentically human
- whether an audience will respond to it

## 3. Saturation is ambiguous
A high baseline can mean:
- the skill is already good
- the benchmark is too weak
- the benchmark only checks easy surface properties

Do not assume a 100% baseline means there is nothing left to improve.

## 4. Meta-skills need proxy benchmarks
Some skills do not produce outputs directly. They shape how other skills behave. These require downstream or proxy benchmarks.

## 5. Portability vs specialization is a trade-off
A mutation can make a skill more portable while weakening platform-specific performance.

## Practical rule
Use scores as evidence, not as truth.
