# Module Map

## Ringkasan Modul

```text
Inbox/CS
  ↓
Catalog/Product
  ↓
Order Chat + QRIS
  ↓
Payment + Follow-Up
  ↓
Finance Dashboard
  ↓
Retention / Repeat Order
  ↓
Social Media Content
```

## 1. Inbox / CS

Menangani pesan customer yang belum terstruktur.

Input:

- DM/chat customer
- komentar IG
- pertanyaan harga/menu
- komplain

Output:

- intent label
- draft reply
- next action

Skill:

- `sorea-inbox-cs-replies`

Agent:

- `inbox-cs-agent`

## 2. Catalog / Product

Menangani data produk/menu.

Input:

- request menu
- search produk
- update stok/harga

Output:

- list menu
- detail produk
- SKU untuk order

Skill:

- `sorea-catalog-products`

Agent:

- `catalog-order-operator`

## 3. Order Chat + QRIS

Menangani order dari chat sampai pembayaran.

Input:

- nama customer
- item + qty
- fulfillment
- alamat/catatan

Output:

- order code
- QRIS
- payment status

Skill:

- `sorea-order-chat-flow`

Agent:

- `catalog-order-operator`

## 4. Payment + Follow-Up

Menangani status pembayaran setelah QRIS dibuat.

Input:

- customer claim sudah bayar
- order code
- webhook/dashboard payment status

Output:

- payment status summary
- customer-safe reply
- follow-up action if pending

Skill:

- `sorea-order-chat-flow`

Agent:

- `catalog-order-operator`

## 5. Finance

Menangani transaksi harian.

Input:

- pemasukan
- pengeluaran
- piutang
- pembayaran piutang
- request rekap

Output:

- catatan transaksi
- rekap laba sederhana
- daftar piutang aktif

Skill:

- `sorea-finance-dashboard`

Agent:

- `finance-operator`

## 6. Social Media / Promotion

Menangani konten promosi.

Input:

- objective promosi
- produk target
- format feed/story
- asset existing atau generate

Output:

- content plan
- caption
- prompt visual
- asset/post/story

Skill:

- `sorea-ig-social-media`
- `sorea-brand-visuals`

Agent:

- `social-media-manager`

## Cross-Handoff Rules

- Inbox menemukan order intent → Catalog Order.
- Catalog question becomes order → Order Chat.
- Order created → Payment + Follow-Up.
- Order paid → Finance if manual finance sync is needed.
- Produk sering ditanya → Social Media untuk ide konten.
- Komplain berat → Inbox CS escalate ke owner.
- Perubahan sistem → Workflow Orchestrator.
