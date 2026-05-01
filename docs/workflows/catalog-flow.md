# Workflow - Catalog and Product

## Goal

Membuat customer dan owner bisa mengakses informasi menu/produk SOREA dengan cepat: list menu, harga, stok, kategori, dan detail produk.

## Commands Covered

- `/katalog_list`
- `/katalog_ready`
- `/katalog_cari <query>`
- `/katalog_kategori <category>`
- `/produk_detail <sku>`
- `/produk_harga <sku> <harga>`
- `/produk_stok <sku> <ready|habis|preorder>`
- natural: `menu apa aja kak?`, `matcha ready?`, `harga fries berapa?`

## Source of Truth

1. Dashboard/MCP catalog tools when available.
2. `data/seeds/products.jsonl` for demo/fallback/reference.

Customer-facing replies should normally show only active and ready products.

## Flow - Customer Asks Menu

1. Detect intent `tanya_menu`.
2. Load ready products.
3. Group by category.
4. Reply with product name and price.
5. Add short order example.

Example output:

```text
Ini menu yang ready kak:

Minuman:
- SOREA Matcha Cream — Rp22.000
- SOREA Kopi Susu — Rp18.000

Snack:
- French Fries — Rp16.000

Kalau mau pesan, tulis aja nama + menu + jumlah ya kak.
```

## Flow - Product Search

1. Match query against SKU, name, alias, or category.
2. If one clear match, show detail.
3. If multiple matches, show candidates.
4. If no match, suggest `/katalog_list`.

## Flow - Owner Updates Product

1. Confirm request is owner/admin context.
2. Validate SKU.
3. Validate field/value.
4. Update via dashboard/MCP if available.
5. Reply with before/after summary if available.

## Safety

- Do not invent prices.
- Do not show unavailable products to customers unless asked.
- Destructive product deletion must require explicit confirmation.
- If product source is fallback/demo, say so when relevant to owner.

## Handoff

- Customer wants to order → `order-chat-flow`.
- Product data issue → `workflow-orchestrator` or dashboard maintainer.
- Product chosen for promo → `ig-social-media` + `brand-visuals`.
