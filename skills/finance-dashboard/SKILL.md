---
name: sorea-finance-dashboard
description: Handle SOREA finance workflows: /keu_start, /keu_input, /keu_piutang, /keu_rekap, /keu_dashboard, natural income/expense/receivable messages, dashboard-origin callbacks, and MCP umkm-finance tools.
---

# SOREA Finance Dashboard Skill

## Use When

- `/keu_*`
- `pemasukan`, `pengeluaran`, `piutang`, `ngutang`, `bayar`, `rekap`, `laba`
- dashboard-origin prompt with `[dashboard_run_id=...]`

## Source of Truth

Use live dashboard via MCP `umkm-finance` when available.

Do not create new finance records in local JSONL if MCP/dashboard is available.

## Intent Mapping

- income/expense → `umkm_catat_pemasukan_pengeluaran`
- new receivable → `umkm_catat_piutang_baru`
- receivable payment → `umkm_catat_pembayaran_piutang`
- recap → `umkm_ambil_rekap`
- health/debug → `umkm_health_check`
- dashboard callback → `umkm_notify_dashboard`

## Parsing Rules

- `60rb` → `60000`
- `10k` → `10000`
- `1jt` → `1000000`
- If date says `kemarin`, convert to absolute date using current timezone.
- If amount is missing/ambiguous, ask clarification.

## Workflow - Income/Expense

1. Detect type.
2. Parse amount.
3. Extract category/note.
4. Call MCP tool.
5. Confirm with rupiah, type, note, date.

## Workflow - Receivable

1. Detect customer name.
2. Parse amount.
3. Extract due date/note if present.
4. Create receivable.
5. Confirm amount and due date.

## Workflow - Receivable Payment

1. Detect customer name or receivable id.
2. Parse payment amount.
3. Call payment tool.
4. Confirm payment.

## Workflow - Recap

1. Determine period: today/week/month.
2. Call recap tool.
3. Summarize total income, expense, profit, transactions, active receivables.

## Dashboard Callback

If prompt contains `[dashboard_run_id=<UUID>]`:

1. Finish the user-facing answer.
2. Call `umkm_notify_dashboard` with that UUID and the reply text.

## Safety

- Never expose tokens/secrets.
- Never invent amount/category/customer.
- Do not delete/edit finance records unless a dedicated safe workflow exists.
