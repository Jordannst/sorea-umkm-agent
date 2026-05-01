# Integration - UMKM Finance Dashboard

## Purpose

Dashboard UMKM adalah integrasi utama untuk menyimpan dan mengelola data operasional SOREA:

- product catalog
- orders
- order items
- QRIS/payment status
- finance transactions
- receivables/piutang
- recap harian/mingguan/bulanan

Repo `sorea-umkm-agent` tidak berisi source dashboard. Repo ini berisi agent layer: role, skills, commands, workflows, rules, dan SOP.

## External Dashboard Repo

Dashboard/web app hidup di project terpisah:

```text
/home/kelompok3/umkm-finance-dashboard
```

Production dashboard URL:

```text
https://umkm-finance-dashboard.vercel.app
```

## MCP Server

Agent berkomunikasi dengan dashboard lewat MCP server bernama:

```text
umkm-finance
```

Example config lives in:

```text
.mcp.json.example
config/env.example
```

Do not commit real secrets.

## MCP Tool Map

### Finance

| Agent workflow | MCP tool |
| --- | --- |
| Catat pemasukan/pengeluaran | `umkm_catat_pemasukan_pengeluaran` |
| Catat piutang baru | `umkm_catat_piutang_baru` |
| Catat pembayaran piutang | `umkm_catat_pembayaran_piutang` |
| Ambil rekap | `umkm_ambil_rekap` |
| Health check | `umkm_health_check` |

### Catalog and Order

| Agent workflow | MCP tool |
| --- | --- |
| Cari/list produk | `umkm_catalog_search` |
| Buat order | `umkm_create_order` |
| Generate QRIS | `umkm_generate_qris` |
| Cek order/status | `umkm_order_get` |

### Dashboard Chat Callback

| Agent workflow | MCP tool |
| --- | --- |
| Notify dashboard answer done | `umkm_notify_dashboard` |

## Main Data Flows

### Catalog Flow

```text
customer asks menu
→ agent calls catalog search/list
→ dashboard returns active/ready products
→ agent replies with menu bullets
```

### Order + QRIS Flow

```text
customer orders via chat
→ agent parses name/items/fulfillment
→ agent resolves products to SKU
→ agent creates order in dashboard
→ agent generates QRIS
→ agent replies with order summary + QR image
```

### Payment Flow

```text
customer pays QRIS
→ Pakasir/payment webhook updates dashboard
→ dashboard stores paid status
→ dashboard can notify customer if Telegram contact id exists
→ agent can check order status via MCP
```

### Finance Flow

```text
owner sends finance input
→ agent parses type/amount/note/customer
→ agent writes via MCP
→ dashboard becomes source of truth
→ agent reads recap from dashboard
```

## Source-of-Truth Rules

- Finance data: dashboard/MCP is source of truth.
- Catalog/order data: dashboard/MCP is source of truth when available.
- Seed data in `data/seeds/products.jsonl` is demo/fallback/reference only.
- Payment status must come from dashboard/webhook or explicit owner-confirmed fallback.

## Important Safety Rules

- Do not commit dashboard secrets/API keys/tokens.
- Do not send dashboard admin URLs to customer.
- Do not mark order as paid based only on customer claim.
- Do not edit deployed dashboard source from this agent repo.
- If dashboard behavior needs code change, propose change in docs/handoff and implement in dashboard repo separately.

## Related Repo Files

- `skills/finance-dashboard/SKILL.md`
- `skills/catalog-products/SKILL.md`
- `skills/order-chat-flow/SKILL.md`
- `agents/finance-operator.md`
- `agents/catalog-order-operator.md`
- `docs/workflows/finance-flow.md`
- `docs/workflows/catalog-flow.md`
- `docs/workflows/order-flow.md`
- `docs/workflows/payment-follow-up-flow.md`
- `rules/source-of-truth.md`
- `.mcp.json.example`
- `config/env.example`
