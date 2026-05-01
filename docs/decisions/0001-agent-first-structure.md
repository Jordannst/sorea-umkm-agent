# Decision 0001 - Agent-First Repo Structure

## Status

Accepted.

## Context

SOREA membutuhkan agent yang tidak hanya menjawab chat, tapi bisa menjalankan workflow lintas domain: customer service, catalog, order, payment, finance, dan social media.

Jika semua instruksi diletakkan di satu prompt panjang, sistem sulit dirawat, sulit dievaluasi, dan mudah lupa SOP spesifik.

## Decision

Gunakan struktur agent-first:

- `agents/` untuk role/domain owner.
- `skills/` untuk SOP modular.
- `docs/` untuk dokumentasi arsitektur, command, demo, dan workflow.
- `data/` untuk seed/sample.
- `memory/` untuk progress historis.

## Consequences

Positive:

- mudah dinilai karena role dan skill terlihat jelas
- workflow reusable
- mudah tambah modul baru
- handoff antar-agent lebih rapi

Tradeoff:

- butuh disiplin dokumentasi
- beberapa informasi tersebar di beberapa file, sehingga perlu index yang jelas

## Follow-up

- Tambahkan skill baru jika ada modul baru.
- Jangan membuat skill terlalu panjang; pindahkan detail ke docs/references bila perlu.
- Update `docs/commands.md` saat command baru ditambahkan.
