#!/usr/bin/env python3
"""Print a clean tree for the SOREA UMKM Agent repo."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORE = {'.git', '__pycache__', '.DS_Store'}


def tree(path: Path, prefix: str = '') -> None:
    entries = sorted([p for p in path.iterdir() if p.name not in IGNORE], key=lambda p: (not p.is_dir(), p.name.lower()))
    for index, entry in enumerate(entries):
        connector = '└── ' if index == len(entries) - 1 else '├── '
        print(prefix + connector + entry.name)
        if entry.is_dir():
            extension = '    ' if index == len(entries) - 1 else '│   '
            tree(entry, prefix + extension)


if __name__ == '__main__':
    print(ROOT.name + '/')
    tree(ROOT)
