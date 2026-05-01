# Workflow - Inbox / Customer Service

## Goal

Membantu owner merespons chat customer dengan cepat, natural, dan terarah.

## Covered Inputs

- WhatsApp/Telegram/IG DM style customer messages
- IG comments needing reply
- owner asks: `draft balasan untuk customer ini`
- natural customer questions about menu, price, order, payment, complaint

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

## Flow

1. Read latest customer message and short context if available.
2. Summarize the message in one line.
3. Classify intent and urgency.
4. Draft reply in SOREA tone.
5. Recommend next action.
6. If facts are needed, route to catalog/order/finance source instead of guessing.

## Owner Review Output

```text
Intent: [label]
Urgency: [low/normal/high]
Summary: [one line]
Draft reply:
[reply]
Next action: [action]
```

## Direct Customer Reply Output

If the active workflow is direct customer reply, send only the customer-facing message.

Example:

```text
Boleh kak, ini menu yang ready hari ini ya...
```

## Escalation Rules

Escalate to owner if:

- customer asks refund/compensation
- customer is angry or complaint is high urgency
- payment/order facts are unclear
- policy decision is needed

## Handoff

- Menu/price/stok → `catalog-products`.
- New order → `order-chat-flow`.
- Payment/order status → `order-chat-flow` and dashboard.
- Finance/receivable issue → `finance-dashboard`.
- IG-specific comment/DM → `ig-social-media` if content context is needed.
