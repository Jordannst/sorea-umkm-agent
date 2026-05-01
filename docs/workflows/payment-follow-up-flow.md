# Workflow - Payment and Follow-Up

## Goal

Menjelaskan alur setelah order dibuat: QRIS, status pembayaran, notifikasi customer, dan follow-up.

## Commands Covered

- `/bayar <order_code>`
- natural: `sudah bayar kak`, `order saya sudah lunas?`, `cek pembayaran ORD-...`

## Flow - QRIS Payment

1. Order is created from `/pesan` or natural order chat.
2. Agent generates QRIS.
3. Customer scans and pays.
4. Payment provider webhook updates dashboard payment status.
5. Dashboard can notify customer automatically if customer contact was saved.
6. Agent/owner can check status via order tool/dashboard.

## Flow - Customer Says Already Paid

1. Ask/order code if missing.
2. Query order status from dashboard/MCP.
3. If paid, reply confirmed.
4. If still pending, reply politely that system has not confirmed yet and suggest waiting/checking payment proof according to owner workflow.

## Manual Fallback

Manual confirmation is fallback only.

Use only when:

- owner explicitly confirms payment outside QRIS/webhook, or
- dashboard/payment provider has a known outage and owner instructs manual handling.

## Safety

- Do not mark paid based only on customer claim.
- Do not repeatedly poll unless requested.
- Do not expose internal payment/admin URLs.
- Keep payment reply short and calm.

## Handoff

- Paid order → finance recap/income workflow if manual sync is needed.
- Pending order after long wait → owner/customer follow-up.
- Payment provider issue → workflow orchestrator/dashboard maintainer.
