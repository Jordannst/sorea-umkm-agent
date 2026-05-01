# Finance Commands

## `/keu_start`

Menampilkan bantuan command finance.

## `/keu_input <type> <amount> <note>`

Mencatat pemasukan atau pengeluaran.

Examples:

```text
/keu_input pemasukan 60000 jual matcha
/keu_input pengeluaran 25000 beli susu
```

Natural examples:

```text
pemasukan 60rb jual kopi susu
pengeluaran 25k beli susu dan es batu
```

## `/keu_piutang`

Mencatat piutang baru atau pembayaran piutang.

Examples:

```text
Budi ngutang 200rb tempo Jumat
Budi bayar 100rb
```

## `/keu_rekap <today|week|month>`

Mengambil rekap dashboard.

## `/keu_dashboard`

Memberikan link dashboard finance.

## Safety

- Jangan invent nominal.
- Jangan catat kalau type/amount/customer ambigu.
- Dashboard/MCP adalah source of truth.
