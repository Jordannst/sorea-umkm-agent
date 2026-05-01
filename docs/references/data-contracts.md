# Data Contracts

Dokumen ini merangkum bentuk data yang dipakai agent untuk berpikir dan handoff. Implementasi database production bisa berbeda, tapi konsep field harus tetap konsisten.

## Product

```json
{
  "sku": "P004",
  "name": "SOREA Matcha Cream",
  "category": "Drink",
  "price": 18000,
  "stock_status": "ready",
  "is_active": true,
  "description": "Minuman matcha creamy khas SOREA"
}
```

## Order

```json
{
  "order_code": "ORD-YYYYMMDD-001",
  "customer_name": "Jordan",
  "items": [
    { "sku": "P004", "name": "SOREA Matcha Cream", "qty": 1, "unit_price": 18000 }
  ],
  "fulfillment_method": "Ambil di tempat",
  "address": null,
  "notes": "less ice",
  "order_status": "menunggu_pembayaran",
  "payment_status": "pending",
  "total_amount": 18000
}
```

## Finance Transaction

```json
{
  "type": "income",
  "amount": 60000,
  "category_name": "penjualan",
  "note": "jual matcha",
  "transaction_date": "YYYY-MM-DD"
}
```

## Receivable

```json
{
  "customer_name": "Budi",
  "amount": 200000,
  "paid_amount": 100000,
  "remaining_amount": 100000,
  "due_date": "YYYY-MM-DD",
  "status": "active"
}
```

## Inbox Classification

```json
{
  "intent": "tanya_menu",
  "urgency": "normal",
  "summary": "Customer menanyakan menu yang tersedia",
  "draft_reply": "Ini menu yang ready kak...",
  "next_action": "send_catalog"
}
```
