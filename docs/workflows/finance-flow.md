# Workflow - Finance Dashboard

## Goal

Membuat owner bisa mencatat keuangan harian lewat chat dengan input natural.

## Supported Intents

- pemasukan
- pengeluaran
- piutang baru
- pembayaran piutang
- rekap hari ini/minggu ini/bulan ini

## Flow Income/Expense

1. Parse jenis transaksi.
2. Parse nominal.
3. Parse catatan/kategori.
4. Call dashboard/MCP finance tool.
5. Reply konfirmasi.

Example:

```text
pemasukan 60rb jual matcha
```

Output:

```text
Tercatat ✅
Pemasukan: Rp60.000
Catatan: jual matcha
```

## Flow Piutang Baru

Example:

```text
Budi ngutang 200rb untuk pesanan kantor, tempo minggu depan
```

Agent:

- customer = Budi
- amount = 200000
- note = pesanan kantor
- due date = absolute date if possible

## Flow Pembayaran Piutang

Example:

```text
Budi bayar 100rb
```

Agent:

- find active receivable by customer name
- record payment
- confirm remaining status if available

## Flow Rekap

Example:

```text
/keu_rekap today
```

Output:

- total pemasukan
- total pengeluaran
- laba sederhana
- jumlah transaksi
- piutang aktif
- transaksi terbaru

## Safety

- Jangan invent nominal.
- Kalau nominal ambigu, tanya klarifikasi.
- Jangan mencatat finance lokal jika dashboard/MCP tersedia.
- Edit/delete transaksi belum menjadi default chat workflow; minta owner gunakan dashboard atau konfirmasi workflow khusus.
