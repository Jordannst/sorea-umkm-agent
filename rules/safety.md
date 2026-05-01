# Safety Rules

## Secrets

- Jangan commit API key, token, password, cookie, atau credential.
- `.mcp.json.example` boleh berisi placeholder env saja.
- `TOOLS.md` hanya menyimpan nama env/config, bukan nilai secret.

## External Actions

Perlu intent eksplisit untuk:

- posting Instagram
- broadcast/message eksternal
- update data penting
- mark payment/order status
- delete product/transaction

## Payments

- Jangan mark paid tanpa status valid dari webhook/dashboard atau owner-confirmed manual workflow.
- Jangan kirim admin dashboard URL ke customer.
- QRIS customer-facing harus berupa image/summary aman.

## Finance

- Jangan invent amount/category/customer.
- Jika amount ambigu, tanya klarifikasi.
- Edit/delete transaksi bukan default workflow.
