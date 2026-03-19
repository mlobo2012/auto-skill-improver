# Eval Patterns

These are starter patterns, not universal laws.

## Execution skills
- Does the plan use a real backend or tool?
- Does the command execute successfully?
- Does the output mention the requested target or resource?
- Does fallback trigger correctly when the primary path fails?
- Does the plan avoid unnecessary extra steps?

## Routing skills
- Is the highest-priority valid route selected?
- Are weaker routes avoided when a better one exists?
- Are required parameters present?
- Is the safe fallback selected when constraints apply?

## Artifact skills
- Does the artifact contain all required sections?
- Does it open, render, or parse successfully?
- Are required metadata fields present?
- Are placeholders absent?
- Are dependency failures handled explicitly?

## Formatting/content skills
- Does the output match the requested mode?
- Does it preserve the required structure?
- Does it avoid known anti-patterns?
- Does it handle ambiguous prompts consistently?
- Does it avoid conflicts with sibling instruction layers?

## Research/audit skills
- Are required sections present?
- Are claims tied to evidence or examples?
- Are unsupported claims absent?
- Are recommendations prioritized?
- Are limitations acknowledged?

## Meta-skills
Use proxy benchmarks.
- Does the downstream target improve?
- Does the mutation resolve known conflicts?
- Does it avoid regressions on held-out prompts?

## Regression guards
Always include at least one guard against breaking something else.
Examples:
- preserves tool guidance
- preserves safety caveats
- preserves anti-pattern rules
- does not remove fallback behavior
