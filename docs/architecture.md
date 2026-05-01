# Architecture - SOREA UMKM Agent

## High-Level View

```text
Customer/Owner Chat
        ↓
Liana Agent Router
        ↓
agents/ role selection
        ↓
skills/ workflow execution
        ↓
Dashboard / MCP / Browser / Data files
        ↓
Reply, QRIS, recap, content, or handoff
```

## Komponen

### 1. Chat Layer

Tempat owner/customer berinteraksi. Bisa berupa Telegram, WhatsApp, IG DM, atau dashboard chat. Untuk demo saat ini Telegram dan dashboard chat menjadi jalur utama.

### 2. Agent Router

Agent memilih role berdasarkan intent:

- customer bertanya menu → Inbox/CS atau Catalog Order
- customer pesan → Catalog Order
- owner catat uang → Finance
- owner minta konten → Social Media
- owner minta rapihin repo → Workflow Orchestrator

### 3. Skills

Skill adalah SOP modular. Skill tidak harus berisi semua konteks besar, cukup instruksi kerja yang membuat agent konsisten.

Contoh:

- `order-chat-flow` tahu kapan harus search catalog, create order, generate QRIS.
- `finance-dashboard` tahu tool MCP mana yang dipakai untuk income/expense/piutang.
- `ig-social-media` tahu branch antara planning, generate visual, feed, atau story.

### 4. Dashboard / MCP Tools

Dashboard menjadi pusat data operasional:

- products
- orders
- payments
- finance transactions
- receivables
- recap

MCP tools menjadi jembatan agar agent bisa membaca/menulis data dashboard tanpa membuka UI manual.

Detail integrasi dashboard/MCP ada di `../integrations/umkm-dashboard.md`.

### 5. Documentation + Memory

Repo ini menyimpan SOP, keputusan desain, dan konteks agar sistem bisa dilanjutkan oleh agent atau developer lain.

## Data Flow Utama

### Order

```text
chat order → parse → catalog search/SKU → create order → generate QRIS → reply QR → payment webhook → dashboard paid status
```

### Finance

```text
owner input → parse type/amount/category → MCP finance write → dashboard transaction → recap
```

### Social Media

```text
content goal → plan → visual branch → generate/use asset → caption → post/prepare → verify/log
```

## Design Boundary

Repo ini bukan menggantikan dashboard app. Repo ini adalah **agent operating layer**:

- menyimpan role, skill, dan SOP
- menjelaskan integrasi
- menyediakan seed/sample
- mendukung demo dan evaluasi

Implementasi production UI/API tetap berada di dashboard project terpisah.
