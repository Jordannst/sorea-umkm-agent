---
name: sorea-ig-social-media
description: Handle SOREA Instagram/social media workflows: /ig_start, /ig_plan, /ig_generate, /ig_post, /ig_story, planning, visual generation, captions, publishing, verification, and issue recovery.
---

# SOREA IG Social Media Skill

## Use When

- `/ig_*` or `/insta_*`
- Instagram feed/story/reels idea
- content planning
- visual generation
- caption/hashtag
- publish/verification

## Inputs to Gather

- objective: promo, menu highlight, review, awareness, order reminder
- format: feed, story, carousel, reels idea
- product/menu focus
- asset mode: existing or generate
- CTA
- publish now or prepare draft

## Workflow

1. If cold start, identify branch first.
2. Plan before generating/posting unless user gave exact instruction.
3. Apply brand rules from `sorea-brand-visuals`.
4. Create caption/visual prompt.
5. If generating, save asset path and describe usage.
6. If posting, use available API/browser path and verify result.
7. Log blocker if publish fails.

## Commands Covered

- `/ig_start` → warm start and quick options.
- `/ig_plan` → content idea + caption angle + CTA.
- `/ig_generate` → visual prompt/asset generation.
- `/ig_post` → feed post from existing/generated asset.
- `/ig_story` → story post.

## Branches

- plan only
- generate visual
- feed post
- story post
- verify/log result

## Caption Output

Include:

- hook
- short body
- CTA
- optional hashtags

Keep it natural, not too salesy.

## Visual Generation Output

Include:

- prompt
- aspect ratio recommendation
- text overlay suggestion
- logo usage note

## Safety / Publish Rules

- Public posting requires explicit user intent.
- Do not claim success without verification.
- If same step fails twice, stop and inspect.
- Browser status source can be direct CDP endpoint if configured.

## Handoff

- Product facts/price → catalog skill.
- Customer comments/DM replies → inbox CS skill.
- Brand consistency → brand visuals skill.
