# Workflow - Order Chat + QRIS

## Goal

Membuat customer bisa pesan lewat chat natural, lalu agent membuat order dan mengirim QRIS.

## Required Fields

- customer name
- items and quantities
- fulfillment method: ambil/antar
- address if delivery
- optional notes

## Flow

1. Terima pesan customer.
2. Deteksi apakah pesan hanya greeting/menu/order.
3. Kalau menu: tampilkan katalog ready.
4. Kalau order: parse customer name, item, qty, fulfillment.
5. Kalau ada field wajib kurang, tanya satu follow-up paling penting.
6. Search catalog untuk resolve nama produk ke SKU.
7. Create order di dashboard.
8. Generate QRIS.
9. Kirim ringkasan order + QRIS.
10. Tunggu payment webhook/status.

## Natural Language Examples

```text
mau matcha 1 fries 1
```

Missing name and fulfillment → ask:

```text
Siap kak. Atas nama siapa, dan mau ambil di tempat atau diantar?
```

```text
Nama Dinda, kopi susu 2, antar ke kos belakang kampus
```

Enough detail → create order.

## Reply Format After Order Created

```text
Pesanan berhasil dibuat kak ✅

Order: ORD-YYYYMMDD-XXX
Atas nama: [nama]
Item:
- [produk] x[jumlah]

Total produk: Rp[amount]
Status: Menunggu pembayaran

Silakan scan QRIS berikut ya kak.
```

Attach QR image when possible.

## Safety

- Jangan buat order jika nama customer tidak ada.
- Jangan tebak produk jika search ambiguous.
- Jangan kirim admin dashboard URL ke customer.
- Jangan mark paid manual kecuali owner jelas meminta dan status valid.
- Untuk Telegram-origin order, simpan chat id agar notifikasi pembayaran otomatis bisa dikirim.
