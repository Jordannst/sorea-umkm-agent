---
name: sorea-catalog-products
description: Handle SOREA catalog/product workflows: list menu, search product, show price/detail/stock/category, answer menu questions, and guide owner/admin product updates for /katalog_* and /produk_* commands.
---

# SOREA Catalog Products Skill

## Use When

- customer asks menu/products/prices/stock
- `/katalog_*` command appears
- `/produk_*` command appears
- order flow needs SKU resolution

## Commands Covered

- `/katalog_list`
- `/katalog_ready`
- `/katalog_cari <query>`
- `/katalog_kategori <category>`
- `/produk_detail <sku>`
- `/produk_harga <sku> <harga>`
- `/produk_stok <sku> <ready|habis|preorder>`

## Source of Truth

Preferred:

1. Dashboard/MCP catalog tools when available.
2. `data/seeds/products.jsonl` for demo/fallback/reference.

Customer-facing replies should show only active/ready products unless owner asks otherwise.

## Workflow - List Menu

1. Load/search catalog.
2. Group by category if possible.
3. Show product name and price.
4. Mention availability if needed.
5. End with simple order example.

## Workflow - Search Product

1. Match by SKU, product name, or common alias.
2. If exactly one clear match, show detail.
3. If multiple matches, list candidates and ask customer to choose.
4. If no match, suggest menu list.

## Workflow - Update Product

1. Confirm the requester is owner/admin context.
2. Validate SKU and field.
3. For price, parse rupiah integer.
4. For stock, restrict to known statuses: `ready`, `habis`, `preorder`.
5. Confirm result.

## Output Rules

- Use Indonesian.
- Use bullets, not markdown tables for chat.
- Format price as `Rp18.000`.
- Keep replies short.

## Example Reply

```text
Ini menu yang ready kak:

Minuman:
- SOREA Matcha Cream — Rp18.000
- Kopi Susu SOREA — Rp16.000

Snack:
- French Fries — Rp15.000

Kalau mau pesan, tulis aja: Nama, menu, jumlah, ambil/antar.
```

## Safety

- Do not invent price or stock.
- Destructive removal needs explicit confirmation.
- If dashboard/catalog unavailable, say using demo catalog if applicable.
