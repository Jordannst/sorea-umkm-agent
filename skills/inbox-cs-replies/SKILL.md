---
name: sorea-inbox-cs-replies
description: Classify SOREA customer messages, detect customer intent, draft short natural Indonesian replies, and route to catalog, order, payment, finance, or social workflows.
---

# SOREA Inbox CS Replies Skill

## Use When

- customer asks menu/price/stock
- customer wants to order
- customer complains
- customer asks payment/order status
- owner asks for reply draft
- IG DM/comment needs response

## Intent Labels

- `tanya_menu`
- `tanya_harga`
- `tanya_stok`
- `order_baru`
- `repeat_order`
- `payment_question`
- `lokasi_jam_buka`
- `promo`
- `komplain`
- `unclear`

## Workflow

1. Summarize the customer message in one line.
2. Classify intent.
3. Decide urgency: low, normal, high.
4. Draft reply in SOREA tone.
5. Recommend next action.

## Reply Tone

- warm
- helpful
- concise
- natural Indonesian
- no stiff corporate language

## Output Format for Owner Review

```text
Intent: [label]
Urgency: [low/normal/high]
Summary: [one line]
Draft reply:
[reply]
Next action: [action]
```

## Auto Reply Style

If replying directly to customer, only send the reply text, not the analysis labels.

## Examples

Customer:

```text
menu apa aja kak?
```

Reply:

```text
Boleh kak, ini menu yang ready hari ini ya...
```

Customer:

```text
pesanan saya kok belum sampai?
```

Draft:

```text
Maaf ya kak, boleh kirim nomor order atau atas nama pesanannya? Biar kami cek statusnya dulu.
```

## Safety

- Do not promise compensation/refund without owner approval.
- Do not argue with customer.
- Escalate serious complaints.
- If order/payment facts are needed, query the relevant source instead of guessing.
