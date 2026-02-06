
# Phase 20 Guide — Production Connector Pattern

## 1) Initialize DB
python backend/app/init_db_phase20.py

## 2) Webhooks
POST /webhooks/{provider}
Providers supported (scaffold):
- paystack
- flutterwave
- stripe

Set secret to enforce signature checks:
NOETIVIS_PAYSTACK_WEBHOOK_SECRET=...
NOETIVIS_FLUTTERWAVE_WEBHOOK_SECRET=...
NOETIVIS_STRIPE_WEBHOOK_SECRET=...

Headers supported (choose one depending on provider):
- X-Signature: <hex hmac sha256>
- X-Signature-Sha512: <hex hmac sha512>

## 3) Wallet
GET /wallet/me

## 4) Reconciliation (founder)
GET /reconcile/wallet-txns
