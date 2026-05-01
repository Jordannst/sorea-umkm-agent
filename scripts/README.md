# Scripts

Helper script kecil untuk audit repo. Script ini aman: tidak call API, tidak butuh secrets, dan tidak mengubah data production.

## Available Scripts

### `print_structure.py`

Print tree repo rapi untuk laporan/presentasi.

```bash
python3 scripts/print_structure.py
```

### `validate_repo.py`

Validasi file penting, agents, skills, workflow docs, frontmatter skill, dan seed product JSONL.

```bash
python3 scripts/validate_repo.py
```

### `check_workflows.py`

Cek coverage workflow utama: `/ig_*`, `/keu_*`, `/katalog_*`, `/produk_*`, `/pesan`, `/bayar`, dan inbox/CS.

```bash
python3 scripts/check_workflows.py
```
