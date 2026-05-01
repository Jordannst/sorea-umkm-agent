# MEMORY.md - SOREA UMKM Core Knowledge

## Brand
- SOREA is a modern local beverage UMKM brand.
- Brand vibe: warm, fresh, soft, modern, clean, aesthetic, premium-light.
- Audience: Gen Z, students, young workers, social-media-first buyers.
- Colors: sage green, cream, white, peach, soft brown.
- Voice: friendly, concise, inviting, not too salesy.

## Core workflows
- `/ig_*`: Instagram/social media planning, visual generation, feed/story publishing, verification.
- `/keu_*`: daily finance through live dashboard and MCP `umkm-finance`.
- `/katalog_*` and `/produk_*`: SOREA menu/product catalog.
- `/pesan` and `/bayar`: chat-based order and payment confirmation flow.
- Inbox/CS: classify customer intent and draft replies.

## Source of truth
- Finance source of truth: live dashboard + Supabase via MCP.
- Catalog/order source of truth: live dashboard + MCP order/catalog tools when available.
- Product seed data in `data/seeds/products.jsonl` is demo/fallback/reference, not production truth.
- Instagram source: workflow docs/runbooks and Meta/API/browser tools.

## Repo requirement
This repo must include OpenClaw agent root files, plus high-quality `skills/` and `agents/` folders.

## Finalization note
- On 2026-05-01 the repo was expanded into a more complete evaluation-ready structure with detailed README, AGENTS rules, agent role specs, skill SOPs, architecture docs, command map, workflow docs, demo script, evaluation checklist, decision record, and data contracts.
