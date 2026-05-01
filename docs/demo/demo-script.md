# Demo Script - SOREA UMKM Agent

## Tujuan Demo

Menunjukkan bahwa agent bisa membantu UMKM dari chat customer sampai order, pembayaran, keuangan, dan promosi.

## Setup Singkat

Pastikan:

- dashboard bisa diakses
- MCP finance/order tools aktif
- produk seed/demo tersedia
- Telegram/chat route aktif
- QRIS demo Pakasir bisa generate

## Scene 1 - Customer Tanya Menu

Customer:

```text
halo kak, menu apa aja?
```

Expected agent:

- mengenali intent tanya_menu
- mengambil katalog ready
- membalas menu dalam bullet
- memberi contoh cara order

## Scene 2 - Customer Order Natural

Customer:

```text
Nama Jordan, mau Matcha Cream 1 sama French Fries 1, ambil di tempat
```

Expected agent:

- resolve Matcha Cream dan French Fries ke SKU
- create order di dashboard
- generate QRIS
- reply order code, item summary, total, status menunggu pembayaran
- attach QRIS

## Scene 3 - Payment Confirmation

Customer membayar QRIS.

Expected:

- webhook Pakasir update payment status di dashboard
- customer mendapat notifikasi pembayaran diterima bila channel contact tersimpan
- order status bisa dicek dari dashboard/tool

## Scene 4 - Finance Recap

Owner:

```text
/keu_rekap today
```

Expected agent:

- mengambil rekap dashboard
- menampilkan pemasukan, pengeluaran, laba, transaksi, piutang aktif

## Scene 5 - Manual Expense

Owner:

```text
pengeluaran 25000 beli susu dan es batu
```

Expected agent:

- parse sebagai expense
- amount Rp25.000
- catat ke dashboard
- reply konfirmasi

## Scene 6 - Social Media Content

Owner:

```text
/ig_plan promo matcha cream sore ini
```

Expected agent:

- membuat ide konten singkat
- pilih format feed/story
- caption angle
- CTA order

Optional lanjut:

```text
/ig_generate visual promo matcha cream
```

Expected:

- prompt visual sesuai brand SOREA
- asset siap dipakai untuk posting

## Demo Closing

Tekankan bahwa repo ini membuat agent bisa bekerja lintas modul:

```text
Inbox → Catalog → Order → Payment → Finance → Social Media
```

Nilai utama:

- owner tidak perlu input manual berkali-kali
- customer flow lebih cepat
- data masuk dashboard
- workflow bisa dilacak dan dikembangkan
