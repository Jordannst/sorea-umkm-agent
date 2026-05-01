# Commands

Folder ini berisi spesifikasi command chat untuk SOREA UMKM Agent.

Catatan: OpenClaw tidak harus memakai struktur command seperti Claude. Folder ini dibuat sebagai dokumentasi operasional agar evaluator mudah melihat command apa saja yang didukung agent.

## Command Groups

- `catalog.md` — `/katalog_*` dan `/produk_*`
- `order.md` — `/pesan`, `/bayar`, order natural language
- `finance.md` — `/keu_*`
- `instagram.md` — `/ig_*`
- `inbox.md` — customer service / DM / reply draft

## Design Rule

Command adalah shortcut, bukan satu-satunya cara berinteraksi. Agent tetap harus memahami bahasa natural seperti:

- `menu apa aja kak?`
- `Nama Dinda, matcha 1, fries 1, ambil di tempat`
- `pengeluaran 25rb beli susu`
- `buat konten promo matcha cream sore ini`
