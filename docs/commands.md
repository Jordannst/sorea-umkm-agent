# Command Map

Command bersifat shortcut. Agent tetap harus bisa memahami bahasa natural.

## Catalog

### `/katalog_list`
Menampilkan produk ready dalam format bullet.

### `/katalog_ready`
Menampilkan produk yang status stoknya ready.

### `/katalog_cari <query>`
Mencari produk berdasarkan nama/kode/kategori.

### `/katalog_kategori <category>`
Menampilkan produk berdasarkan kategori.

### `/produk_detail <sku>`
Menampilkan detail produk: nama, kategori, harga, status, deskripsi.

### `/produk_harga <sku> <harga>`
Update harga produk. Butuh role owner/admin.

### `/produk_stok <sku> <ready|habis|preorder>`
Update status stok produk. Butuh role owner/admin.

## Order

### `/pesan`
Mulai order. Bisa dengan format lengkap atau natural language.

Contoh lengkap:

```text
/pesan
Nama: Jordan
Pesanan: Matcha Cream 1, French Fries 1
Ambil/antar: Ambil di tempat
Catatan: less ice
```

Contoh natural:

```text
Nama Jordan, matcha cream 1, fries 1, ambil di tempat
```

Agent harus:

1. resolve produk ke SKU
2. create order
3. generate QRIS
4. reply ringkasan + QR

### `/bayar <order_code>`
Cek status pembayaran atau fallback manual confirmation. Payment webhook lebih diutamakan daripada manual.

## Finance

### `/keu_start`
Menampilkan bantuan singkat finance.

### `/keu_input`
Mencatat pemasukan/pengeluaran.

Contoh:

```text
/keu_input pemasukan 60000 jual kopi susu
/keu_input pengeluaran 25000 beli susu
```

Natural juga valid:

```text
pemasukan 60rb jual matcha
pengeluaran 10k beli es batu
```

### `/keu_piutang`
Mencatat piutang baru atau pembayaran piutang.

Contoh:

```text
Budi ngutang 200rb jatuh tempo minggu depan
Budi bayar piutang 100rb
```

### `/keu_rekap <today|week|month>`
Mengambil rekap dari dashboard.

### `/keu_dashboard`
Memberi link dashboard finance.

## Instagram

### `/ig_start`
Warm start workflow IG dan tunjukkan pilihan cepat.

### `/ig_plan`
Membuat rencana konten: objective, format, hook, caption angle, CTA.

### `/ig_generate`
Generate visual promosi menggunakan brand rules SOREA.

### `/ig_post`
Posting feed dari asset yang sudah ada atau hasil generate.

### `/ig_story`
Posting story Instagram.

## Inbox / CS

Tidak wajib slash command. Trigger dari pesan customer:

- “menu apa aja kak?”
- “berapa harga matcha?”
- “bisa antar?”
- “mau order”
- “kok pesanan saya belum sampai?”

Agent harus klasifikasi intent, draft reply, dan route ke modul yang tepat.
