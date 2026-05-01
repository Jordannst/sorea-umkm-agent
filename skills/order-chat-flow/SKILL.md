---
name: sorea-order-chat-flow
description: Handle SOREA chat orders including /pesan, natural-language order parsing, product SKU resolution, dashboard order creation, QRIS generation, payment status guidance, and follow-up handoff.
---

# SOREA Order Chat Flow Skill

## Use When

- `/pesan`, `/order`, `/buat_pesanan`, `/bayar`
- customer says they want to order
- customer gives item + quantity
- customer asks payment/order status
- order needs QRIS

## Required Fields

Before creating order, collect:

- customer name
- product items and quantities
- fulfillment method: pickup or delivery
- address if delivery
- optional notes

Ask only one concise follow-up if required fields are missing.

## Tool/Source Preference

1. Catalog search/resolve from dashboard/MCP.
2. Create order through dashboard/MCP.
3. Generate QRIS through dashboard/MCP.
4. Use JSON/data file only as fallback/reference, not as production source.

## Natural Conversation Handling

### Greeting

Customer:

```text
halo kak
```

Reply:

```text
Halo kak 👋 Mau lihat menu dulu atau langsung pesan?
Kalau mau pesan, bisa tulis: “Matcha Cream 1, French Fries 1, ambil di tempat.”
```

### Menu Request

Call catalog list/search, then reply with menu bullets and order example.

### Order Missing Name

```text
Siap kak. Atas nama siapa ya?
```

### Order Missing Fulfillment

```text
Siap kak. Mau ambil di tempat atau diantar?
```

### Delivery Missing Address

```text
Boleh kak. Untuk antar, boleh kirim alamat lengkapnya?
```

## Order Creation Workflow

1. Parse message.
2. Normalize item aliases.
3. Search catalog and resolve SKU.
4. If ambiguous, ask customer to choose.
5. Create order with SKU + qty.
6. For Telegram-origin orders, pass numeric chat id as `telegram_chat_id` when available.
7. Generate QRIS.
8. Reply with order code, item summary, total, status, and QR image.

## Reply Template

```text
Pesanan berhasil dibuat kak ✅

Order: [order_code]
Atas nama: [customer]
Item:
- [product] x[qty]

Total produk: Rp[amount]
Status: Menunggu pembayaran

Silakan scan QRIS berikut ya kak.
```

## Payment Status

- Prefer webhook/dashboard payment status.
- `/bayar` manual confirmation is fallback only.
- Do not mark paid without valid evidence.

## Safety

- Do not send internal/admin URL to customer.
- Do not invent product totals.
- Do not create order with unknown item.
- Do not repeatedly poll payment status unless explicitly requested.
