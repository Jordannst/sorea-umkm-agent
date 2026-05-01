# Order Commands

## `/pesan`

Membuat order dari chat.

Full format:

```text
/pesan
Nama: Jordan
Pesanan: Matcha Cream 1, French Fries 1
Ambil/antar: Ambil di tempat
Alamat:
Catatan: less ice
```

Natural format:

```text
Nama Jordan, mau matcha cream 1 sama fries 1, ambil di tempat
```

Expected behavior:

1. Parse customer name, items, qty, fulfillment, address, notes.
2. Resolve product names to SKU.
3. Create order in dashboard.
4. Generate QRIS.
5. Reply order summary and QR image.

## `/bayar <order_code>`

Cek status pembayaran atau fallback konfirmasi manual.

Expected behavior:

1. Get order status from dashboard/MCP.
2. Report payment status.
3. Do not mark paid unless valid payment source or owner-confirmed manual workflow.

## Missing Field Prompts

Missing name:

```text
Siap kak. Atas nama siapa ya?
```

Missing fulfillment:

```text
Mau ambil di tempat atau diantar kak?
```

Missing delivery address:

```text
Untuk antar, boleh kirim alamat lengkapnya kak?
```
