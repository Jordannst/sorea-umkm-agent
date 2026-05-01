# Reference Structure Mapping

Repo ini mengambil inspirasi dari dua contoh struktur AI agent, tapi tidak menyalin mentah-mentah karena runtime kita adalah OpenClaw.

## Dari Contoh Claude Code Project

Yang diambil:

- `skills/` as reusable capabilities
- `agents/` as role/subagent definitions
- command specs
- scoped rules
- output/style guidance

Yang tidak diambil mentah:

- `.claude/`
- `CLAUDE.md`
- Claude-specific hooks/plugins/settings

OpenClaw equivalent:

- root `AGENTS.md`, `SOUL.md`, `MEMORY.md`, `TOOLS.md`
- `commands/` sebagai dokumentasi command, bukan Claude slash implementation
- `rules/` sebagai aturan scoped repo

## Dari Contoh Generic AI Agent System

Yang diambil:

- agent core concept
- tools/source-of-truth concept
- workflows
- prompts/templates
- memory
- config example

Yang tidak diambil mentah:

- Python package runtime structure seperti `agent.py`, `planner.py`, `executor.py`
- API server/controllers jika belum menjadi kebutuhan repo ini
- provider implementation code yang sebenarnya ada di dashboard/OpenClaw runtime

OpenClaw equivalent:

- `agents/` menjelaskan role/core logic
- `skills/` menjelaskan executable SOP
- `docs/workflows/` menjelaskan task flow
- `prompts/` menyimpan reusable templates
- `config/` menyimpan contoh env non-secret

## Final Repo Intent

Repo ini harus terlihat sebagai:

```text
OpenClaw-native SOREA UMKM agent workspace
```

Bukan:

```text
Claude project clone
Generic Python agent framework clone
```

Yang paling penting untuk evaluasi:

1. `skills/` kuat, lengkap, dan jelas.
2. `agents/` punya role dan handoff jelas.
3. Docs mendukung demo dan menjelaskan arsitektur.
