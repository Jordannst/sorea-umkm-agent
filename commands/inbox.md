# Inbox / CS Commands

Inbox/CS tidak wajib menggunakan slash command. Modul ini aktif ketika ada pesan customer atau owner minta draft balasan.

## Supported Requests

- `balasin customer ini...`
- `draft reply untuk DM ini...`
- customer asks menu/price/order/status/complaint

## Expected Output for Owner Review

```text
Intent: [label]
Urgency: [low/normal/high]
Summary: [one line]
Draft reply:
[reply]
Next action: [action]
```

## Direct Customer Reply

Jika workflow memang direct reply, kirim hanya reply customer, tanpa label analisis.

## Safety

- Jangan menjanjikan refund/kompensasi tanpa owner approval.
- Komplain serius harus escalate.
- Fakta order/payment harus dicek, bukan ditebak.
