# Evaluation Checklist

Gunakan checklist ini sebelum repo dikumpulkan/dipresentasikan.

## Struktur

- [ ] Root files ada: `AGENTS.md`, `SOUL.md`, `USER.md`, `MEMORY.md`, `IDENTITY.md`, `BOOT.md`, `HEARTBEAT.md`, `TOOLS.md`.
- [ ] Folder `agents/` ada dan berisi role utama.
- [ ] Folder `skills/` ada dan setiap skill punya `SKILL.md` dengan frontmatter valid.
- [ ] Folder `docs/` menjelaskan arsitektur, command, demo, dan workflow.
- [ ] Folder `data/` punya seed/sample data untuk demo.
- [ ] Folder `commands/` menjelaskan slash command/natural command behavior.
- [ ] Folder `rules/` menjelaskan safety, tone, dan source-of-truth.
- [ ] Folder `prompts/` berisi template output reusable.
- [ ] Folder `integrations/` menjelaskan dashboard UMKM dan MCP sebagai integrasi utama.
- [ ] Struktur jelas OpenClaw-native, bukan copy mentah Claude/Python framework.

## Agent Design

- [ ] Setiap agent punya role, owns, responsibilities, inputs, outputs, boundaries, handoff.
- [ ] Ada agent orchestrator untuk koordinasi lintas modul.
- [ ] Role tidak tumpang tindih secara membingungkan.

## Skill Design

- [ ] Setiap skill punya trigger jelas.
- [ ] Setiap skill punya workflow step-by-step.
- [ ] Skill menyebut source of truth dan fallback.
- [ ] Skill punya safety/boundary.
- [ ] Skill bisa dipakai tanpa membaca seluruh repo.

## Workflow Coverage

- [ ] `/ig_*` workflow lengkap: start, plan, generate, post, story, verify.
- [ ] `/keu_*` workflow lengkap: start, input, piutang, rekap, dashboard.
- [ ] `/katalog_*` workflow lengkap: list, ready, search, kategori.
- [ ] `/produk_*` workflow lengkap: detail, harga, stok.
- [ ] `/pesan` workflow lengkap: natural order, SKU resolution, create order, QRIS.
- [ ] `/bayar` workflow lengkap: payment status, webhook preference, manual fallback.
- [ ] Inbox/CS workflow lengkap: intent classification, draft reply, route/handoff.

## Demo Readiness

- [ ] Ada demo script end-to-end.
- [ ] Command utama terdokumentasi.
- [ ] Produk demo tersedia.
- [ ] Catalog/product flow terdokumentasi.
- [ ] Order + QRIS flow terdokumentasi.
- [ ] Payment/follow-up flow terdokumentasi.
- [ ] Finance recap flow terdokumentasi.
- [ ] Social media planning flow terdokumentasi.
- [ ] Inbox/CS flow terdokumentasi.

## Safety

- [ ] Tidak ada secrets/API key/token di repo.
- [ ] `.mcp.json.example` hanya berisi env placeholder.
- [ ] Aksi eksternal/public perlu explicit intent.
- [ ] Payment status tidak diubah tanpa bukti.

## Presentation Points

- [ ] Bisa menjelaskan masalah UMKM yang diselesaikan.
- [ ] Bisa menjelaskan kenapa agent-first.
- [ ] Bisa menunjukkan folder `agents/` dan `skills/` sebagai inti.
- [ ] Bisa menjalankan/menjelaskan demo flow dari chat sampai dashboard.
