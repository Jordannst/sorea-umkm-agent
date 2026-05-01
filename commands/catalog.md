# Catalog Commands

## `/katalog_list`

Menampilkan semua produk aktif/ready.

Expected behavior:

1. Ambil katalog dari dashboard/MCP bila tersedia.
2. Fallback ke `data/seeds/products.jsonl` untuk demo.
3. Kelompokkan berdasarkan kategori.
4. Tampilkan nama dan harga.

## `/katalog_ready`

Menampilkan hanya produk ready.

## `/katalog_cari <query>`

Mencari produk berdasarkan nama, SKU, atau kategori.

Example:

```text
/katalog_cari matcha
```

## `/katalog_kategori <category>`

Menampilkan produk berdasarkan kategori.

Example:

```text
/katalog_kategori Snack
```

## `/produk_detail <sku>`

Menampilkan detail produk.

Example:

```text
/produk_detail P004
```

## `/produk_harga <sku> <harga>`

Update harga produk. Owner/admin only.

## `/produk_stok <sku> <ready|habis|preorder>`

Update status stok produk. Owner/admin only.

## Safety

- Jangan invent harga/stok.
- Customer-facing list hanya tampilkan active/ready.
- Product deletion harus konfirmasi eksplisit.
