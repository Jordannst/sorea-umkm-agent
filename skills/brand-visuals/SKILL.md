---
name: sorea-brand-visuals
description: Apply SOREA brand identity, visual direction, caption tone, logo usage, product photography style, and promo asset guidance for Instagram, catalog, and customer-facing content.
---

# SOREA Brand Visuals Skill

## Use When

- creating captions
- creating promo visuals
- writing Leonardo/image prompts
- designing story/feed concepts
- choosing logo/background style
- reviewing visual consistency

## Brand Personality

- warm
- fresh
- soft
- modern
- clean
- friendly
- premium-light, not luxury-heavy

## Palette

Preferred:

- sage green
- cream
- white
- peach
- soft brown

Avoid:

- harsh neon
- dark heavy background unless intentionally premium
- cluttered red/yellow hard-sell style

## Workflow

1. Identify asset purpose: feed, story, catalog, product photo, promo card, or caption.
2. Choose SOREA visual direction: clean product hero, soft lifestyle, or promo announcement.
3. Apply palette, lighting, logo, and caption voice rules.
4. Produce output: caption, visual prompt, layout note, or review feedback.
5. Check the result against the review checklist before finalizing.

## Visual Rules

- Product must be clear and appetizing.
- Use natural light or soft studio light.
- Keep composition clean.
- Minimal text overlay.
- Logo should support identity, not dominate.
- Prefer lifestyle/product hero scenes.

## Logo Rules

- Use transparent/no-background logo for product photos, watermarks, cup mockups, sticker-style placement, drink visuals, product/feed/promo assets.
- Use profile/background logo for identity cards, intros, profile-style visuals, and brand slides.
- For generated SOREA visuals, use the existing logo asset as reference/overlay; do not let the model invent a lookalike logo.
- If the generated logo differs from the canonical SOREA asset, treat it as a branding miss and regenerate or overlay the canonical logo.
- Do not cover the product with logo.

## Caption Voice

- Indonesian casual-polite.
- Short and warm.
- CTA clear but not pushy.

Good CTA examples:

- `Mau pesan? Chat kami ya kak.`
- `Ready hari ini, bisa ambil di tempat.`
- `Tanya stok dulu boleh banget kak.`

## Prompt Template

```text
Create a clean modern product promotion visual for SOREA [product].
Style: warm, fresh, soft, modern, premium-light UMKM beverage/food brand.
Colors: sage green, cream, white, peach, soft brown.
Lighting: bright natural soft light.
Composition: product hero, minimal layout, appetizing, clean background.
Use the provided canonical SOREA logo reference subtly as product branding/watermark; do not invent or redraw the logo.
No clutter, no harsh sales poster look, no stray foreign text.
```

## Generation Backend Note

For `/ig_generate`, the default visual backend is Leonardo REST v2 `gpt-image-2` with `MEDIUM` quality and the canonical SOREA logo reference selected by asset type.

## Safety

- Do not use misleading product claims.
- Do not overpromise promos, discounts, or stock availability without catalog/owner confirmation.
- Do not place logo/text over critical product details.
- Do not use customer photos/reviews unless owner has permission.

## Review Checklist

- Does the product look clear?
- Does the visual feel SOREA?
- Is the CTA readable?
- Is the logo tasteful?
- Is it suitable for feed/story size?
