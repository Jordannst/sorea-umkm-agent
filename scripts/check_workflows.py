#!/usr/bin/env python3
"""Check that all main SOREA workflows are documented in repo text."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = {
    'instagram': ['/ig_start', '/ig_plan', '/ig_generate', '/ig_post', '/ig_story'],
    'finance': ['/keu_start', '/keu_input', '/keu_piutang', '/keu_rekap', '/keu_dashboard'],
    'catalog': ['/katalog_list', '/katalog_ready', '/katalog_cari', '/katalog_kategori'],
    'product': ['/produk_detail', '/produk_harga', '/produk_stok'],
    'order': ['/pesan'],
    'payment': ['/bayar'],
    'inbox_cs': ['intent', 'draft reply', 'customer', 'komplain'],
}
SEARCH_DIRS = ['README.md', 'AGENTS.md', 'agents', 'skills', 'commands', 'docs', 'rules', 'prompts']


def collect_text() -> str:
    chunks = []
    for rel in SEARCH_DIRS:
        path = ROOT / rel
        if path.is_file():
            chunks.append(path.read_text(encoding='utf-8', errors='ignore'))
        elif path.is_dir():
            for file in path.rglob('*'):
                if file.is_file() and file.suffix in {'.md', '.txt'}:
                    chunks.append(file.read_text(encoding='utf-8', errors='ignore'))
    return '\n'.join(chunks).lower()


def main() -> None:
    text = collect_text()
    missing = {}
    for workflow, terms in WORKFLOWS.items():
        absent = [term for term in terms if term.lower() not in text]
        if absent:
            missing[workflow] = absent
        else:
            print(f'OK: {workflow} workflow covered')
    if missing:
        print('FAIL: missing workflow coverage:')
        for workflow, terms in missing.items():
            print(f'- {workflow}: {terms}')
        sys.exit(1)
    print('PASS: all main workflows are documented')


if __name__ == '__main__':
    main()
