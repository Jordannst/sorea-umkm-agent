#!/usr/bin/env python3
"""Validate required SOREA UMKM Agent repo files and data."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    'README.md', 'AGENTS.md', 'SOUL.md', 'USER.md', 'MEMORY.md', 'IDENTITY.md',
    'BOOT.md', 'HEARTBEAT.md', 'TOOLS.md', '.env.example', '.mcp.json.example', '.gitignore',
    'docs/architecture.md', 'docs/commands.md', 'docs/demo/demo-script.md',
    'docs/evaluation-checklist.md', 'docs/reference-structure-mapping.md',
    'integrations/README.md', 'integrations/umkm-dashboard.md',
    'data/seeds/products.jsonl',
]

REQUIRED_AGENTS = [
    'agents/workflow-orchestrator.md',
    'agents/inbox-cs-agent.md',
    'agents/catalog-order-operator.md',
    'agents/finance-operator.md',
    'agents/social-media-manager.md',
]

REQUIRED_SKILLS = [
    'skills/brand-visuals/SKILL.md',
    'skills/catalog-products/SKILL.md',
    'skills/order-chat-flow/SKILL.md',
    'skills/finance-dashboard/SKILL.md',
    'skills/ig-social-media/SKILL.md',
    'skills/inbox-cs-replies/SKILL.md',
]

REQUIRED_WORKFLOWS = [
    'docs/workflows/module-map.md',
    'docs/workflows/inbox-cs-flow.md',
    'docs/workflows/catalog-flow.md',
    'docs/workflows/order-flow.md',
    'docs/workflows/payment-follow-up-flow.md',
    'docs/workflows/finance-flow.md',
    'docs/workflows/social-content-flow.md',
]


def fail(message: str) -> None:
    print(f'FAIL: {message}')
    sys.exit(1)


def check_exists(paths: list[str], label: str) -> None:
    missing = [p for p in paths if not (ROOT / p).exists()]
    if missing:
        fail(f'missing {label}: {missing}')
    print(f'OK: {label} present ({len(paths)})')


def check_skill_frontmatter() -> None:
    for rel in REQUIRED_SKILLS:
        text = (ROOT / rel).read_text(encoding='utf-8')
        if not text.startswith('---\n') or '\nname:' not in text or '\ndescription:' not in text:
            fail(f'invalid skill frontmatter: {rel}')
    print(f'OK: skill frontmatter valid ({len(REQUIRED_SKILLS)})')


def check_jsonl() -> None:
    path = ROOT / 'data/seeds/products.jsonl'
    count = 0
    for idx, line in enumerate(path.read_text(encoding='utf-8').splitlines(), start=1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            fail(f'invalid JSONL line {idx}: {exc}')
        for key in ['id_produk', 'nama_produk', 'kategori', 'harga', 'stok_status']:
            if key not in item:
                fail(f'missing key {key!r} in product line {idx}')
        count += 1
    if count == 0:
        fail('products.jsonl is empty')
    print(f'OK: product seed JSONL valid ({count} rows)')


def main() -> None:
    check_exists(REQUIRED_FILES, 'root/docs/data files')
    check_exists(REQUIRED_AGENTS, 'agents')
    check_exists(REQUIRED_SKILLS, 'skills')
    check_exists(REQUIRED_WORKFLOWS, 'workflow docs')
    check_skill_frontmatter()
    check_jsonl()
    print('PASS: repository structure looks complete')


if __name__ == '__main__':
    main()
