# Noetivis v20 Master Notes
Includes v19 master + Phase 20 production connector patterns (payments webhooks + wallet reconciliation).

Initialize DB:
  python backend/app/init_db_phase20.py

Webhook secrets (optional but recommended):
  NOETIVIS_PAYSTACK_WEBHOOK_SECRET=...
  NOETIVIS_FLUTTERWAVE_WEBHOOK_SECRET=...
  NOETIVIS_STRIPE_WEBHOOK_SECRET=...
