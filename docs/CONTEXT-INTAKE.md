# Context Intake

One reason internal skill optimization often performs better than public workflows is simple: the internal operator already knows the system around the skill.

To close that gap, Auto Skill Improver should begin by **sponging up the local context** around the target skill.

## Goal
Before benchmarking, collect the minimum context needed to understand what the skill is really trying to do.

## Context sources to inspect
- the target `SKILL.md`
- referenced files linked from the skill
- adjacent skill files in the same directory or family
- example outputs, if they exist
- failure notes or changelogs, if they exist
- environment/tool assumptions described near the skill

## What to extract
- trigger conditions
- output contract
- dependencies and reference files
- fallback behavior
- sibling-skill conflicts
- platform-specific assumptions
- obvious anti-patterns

## Output
Write a compact intake note before mutation with:
- skill classification
- likely failure modes
- benchmark candidates
- regression-guard candidates
- missing context warnings

## Important rule
Do not mutate until the intake pass is complete.

## Why this matters
If you skip context intake, the public workflow underperforms the internal one because it treats skills as isolated text files instead of local operating components.
