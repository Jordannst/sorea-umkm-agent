# SOREA UMKM Agent

> **OpenClaw-native AI agent workspace untuk operasional UMKM SOREA** — dari customer chat, katalog, order, QRIS, keuangan harian, sampai konten Instagram.

SOREA UMKM Agent adalah rancangan **agent-first operating system** untuk membantu owner UMKM menjalankan pekerjaan harian lewat chat, dashboard, dan workflow modular.

Project ini bukan sekadar chatbot. Di dalamnya ada kumpulan **agents**, **skills**, **commands**, **rules**, dan **workflows** yang bekerja sebagai SOP digital untuk bisnis kecil.

---

## Why This Project Exists

Banyak UMKM masih mengelola operasional secara manual:

- customer tanya menu lewat chat
- owner balas satu-satu
- order dicatat manual
- pembayaran dicek manual
- rekap pemasukan/pengeluaran tercecer
- konten promosi dibuat kalau sempat

Repo ini mencoba menjawab masalah itu dengan agent yang bisa membantu alur operasional end-to-end:

```text
Customer Chat
  → Intent Detection
  → Catalog / Product Answer
  → Order Creation
  → QRIS Payment
  → Dashboard Record
  → Finance Recap
  → Social Media Promotion
```

---

## Core Idea: Agent-First UMKM Operations

Pendekatan agent-first berarti pengetahuan bisnis tidak ditumpuk dalam satu prompt panjang. Semua dipisah menjadi bagian yang jelas:

- `agents/` — role agent yang menangani domain tertentu.
- `skills/` — SOP/capability reusable untuk menjalankan workflow.
- `commands/` — command chat seperti `/pesan`, `/keu_rekap`, `/ig_plan`.
- `rules/` — safety, tone, dan source-of-truth rules.
- `prompts/` — template output/caption/visual prompt.
- `docs/workflows/` — alur kerja detail untuk demo dan pengembangan.
- `integrations/` — dokumentasi dashboard/MCP sebagai sistem eksternal penting.

Dengan struktur ini, sistem lebih mudah dipahami, diaudit, dikembangkan, dan dipresentasikan.

---

## Main Capabilities

### Customer Service / Inbox

- Klasifikasi pesan customer.
- Draft balasan natural dalam tone SOREA.
- Routing ke katalog, order, payment, atau finance.
- Escalation untuk komplain atau kasus sensitif.

### Catalog & Product

- Menampilkan menu ready.
- Mencari produk berdasarkan nama/SKU/kategori.
- Menjawab harga dan stok.
- Mendukung update harga/stok untuk owner/admin workflow.

### Chat Order + QRIS

- Parse order dari bahasa natural.
- Resolve nama produk ke SKU.
- Create order ke dashboard.
- Generate QRIS.
- Reply ringkasan order + payment instruction.

### Finance Dashboard

- Catat pemasukan.
- Catat pengeluaran.
- Catat piutang.
- Catat pembayaran piutang.
- Ambil rekap harian/mingguan/bulanan.

### Instagram / Promotion

- Planning konten.
- Caption dan CTA.
- Visual prompt generation.
- Feed/story workflow.
- Brand visual rules untuk SOREA.

---

## Workflow Coverage

| Workflow | Coverage |
| --- | --- |
| `/ig_*` | `/ig_start`, `/ig_plan`, `/ig_generate`, `/ig_post`, `/ig_story` |
| `/keu_*` | `/keu_start`, `/keu_input`, `/keu_piutang`, `/keu_rekap`, `/keu_dashboard` |
| `/katalog_*` | `/katalog_list`, `/katalog_ready`, `/katalog_cari`, `/katalog_kategori` |
| `/produk_*` | `/produk_detail`, `/produk_harga`, `/produk_stok` |
| `/pesan` | Natural order parsing, SKU resolution, order creation, QRIS |
| `/bayar` | Payment status check, webhook-first flow, manual fallback |
| Inbox/CS | Intent classification, draft reply, routing, escalation |

---

## Repository Structure

```text
sorea-umkm-agent/
├── AGENTS.md              # main OpenClaw workspace rules
├── BOOT.md                # startup routine for agent context
├── SOUL.md                # Liana persona and communication style
├── USER.md                # user/project context
├── MEMORY.md              # long-term project memory
├── IDENTITY.md            # agent identity
├── HEARTBEAT.md           # proactive/periodic instruction placeholder
├── TOOLS.md               # environment notes without secrets
├── .env.example           # safe environment placeholder example
├── .mcp.json.example      # MCP config example without real secrets
│
├── agents/                # agent role definitions
├── skills/                # reusable skill/SOP definitions
├── commands/              # chat command specifications
├── rules/                 # safety, tone, source-of-truth, evaluation rules
├── prompts/               # reusable prompt/output templates
├── docs/                  # architecture, workflows, demo, audit docs
├── integrations/          # dashboard/MCP integration docs
├── scripts/               # validation/audit helper scripts
├── config/                # additional config examples
├── data/                  # demo seed data
└── memory/                # development notes
```

---

## Agents

| Agent | Responsibility |
| --- | --- |
| `workflow-orchestrator` | Repo structure, architecture, docs, cross-module handoff. |
| `inbox-cs-agent` | Customer message classification and reply drafting. |
| `catalog-order-operator` | Catalog, product, order, QRIS, payment status. |
| `finance-operator` | Income, expense, receivable, payment, recap. |
| `social-media-manager` | Instagram planning, caption, visual, feed/story workflow. |

See: [`agents/`](agents/)

---

## Skills

| Skill | Purpose |
| --- | --- |
| `sorea-inbox-cs-replies` | Intent detection and customer reply drafting. |
| `sorea-catalog-products` | Catalog/menu/product lookup and product admin guidance. |
| `sorea-order-chat-flow` | Chat order parsing, SKU resolution, order creation, QRIS. |
| `sorea-finance-dashboard` | Finance entries, receivables, recap, dashboard callback. |
| `sorea-ig-social-media` | Instagram plan/generate/post/story workflow. |
| `sorea-brand-visuals` | SOREA brand voice, visual direction, caption and prompt rules. |

See: [`skills/`](skills/)

---

## Dashboard / MCP Integration

Dashboard UMKM adalah integration layer penting untuk project ini.

This repo does **not** contain dashboard source code. Dashboard lives in a separate project/repo and is integrated through MCP tools.

Dashboard handles:

- products
- orders
- order items
- QRIS/payment status
- finance transactions
- receivables
- recaps

Integration docs:

- [`integrations/umkm-dashboard.md`](integrations/umkm-dashboard.md)
- [`.mcp.json.example`](.mcp.json.example)
- [`.env.example`](.env.example)

Source-of-truth rule:

```text
Agent repo = roles, skills, workflows, command behavior, SOP
Dashboard repo = web app, API, database, MCP server, payment implementation
```

---

## Recommended Demo Flow

The strongest demo path:

1. Customer asks for menu.
2. Agent replies with ready catalog.
3. Customer orders naturally, e.g. `Nama Jordan, Matcha Cream 1, French Fries 1, ambil di tempat`.
4. Agent resolves products to SKU.
5. Agent creates order in dashboard.
6. Agent generates QRIS.
7. Customer pays.
8. Dashboard/payment webhook updates payment status.
9. Owner asks for finance recap.
10. Agent helps create promotional Instagram content from the product.

Detailed script: [`docs/demo/demo-script.md`](docs/demo/demo-script.md)

---

## Setup Notes

This repo is mostly documentation/SOP + helper scripts. It is safe to inspect without secrets.

1. Copy environment example only if needed:

```bash
cp .env.example .env
```

2. Fill real secrets locally/server-side only.

3. Never commit `.env`.

`.gitignore` already excludes `.env` and `.env.*` while allowing `.env.example`.

---

## Validation

Helper scripts are included so the repo can be audited quickly.

```bash
python3 scripts/validate_repo.py
python3 scripts/check_workflows.py
python3 scripts/print_structure.py
```

Expected result:

```text
PASS: repository structure looks complete
PASS: all main workflows are documented
```

Scripts are safe:

- no API calls
- no external writes
- no production data mutation
- no secrets required

---

## Documentation Map

Important docs:

- [`docs/architecture.md`](docs/architecture.md) — system architecture.
- [`docs/commands.md`](docs/commands.md) — command map.
- [`docs/workflows/module-map.md`](docs/workflows/module-map.md) — cross-module flow.
- [`docs/workflows/order-flow.md`](docs/workflows/order-flow.md) — order + QRIS flow.
- [`docs/workflows/finance-flow.md`](docs/workflows/finance-flow.md) — finance workflow.
- [`docs/workflows/social-content-flow.md`](docs/workflows/social-content-flow.md) — IG/content workflow.
- [`docs/evaluation-checklist.md`](docs/evaluation-checklist.md) — evaluation checklist.
- [`docs/final-audit-2026-05-01.md`](docs/final-audit-2026-05-01.md) — final audit report.

---

## Why It Is OpenClaw-Native

This repo intentionally does **not** copy Claude-specific or generic Python agent framework structure.

It adapts useful concepts into an OpenClaw workspace:

- OpenClaw root context files: `AGENTS.md`, `SOUL.md`, `MEMORY.md`, `TOOLS.md`.
- `agents/` for role definitions.
- `skills/` for reusable SOP/capabilities.
- `commands/`, `rules/`, `prompts/`, `docs/`, and `integrations/` as supporting layers.

Reference mapping: [`docs/reference-structure-mapping.md`](docs/reference-structure-mapping.md)

---

## Project Status

Status: **finalized initial version for demo/evaluation**.

The repo is ready to be pushed to GitHub as:

```text
sorea-umkm-agent
```

Primary evaluation focus:

```text
agents/
skills/
```

Supporting folders make the repo easier to understand, validate, and present.
