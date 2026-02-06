
# Phase 8 Guide

## 1) Create tables (includes Phase 7 + 8 models)
python backend/app/init_db_phase8.py

## 2) Login using DB auth (Phase 7)
POST /auth/login-db -> Bearer token

## 3) Marketplace purchase writes ledger + payouts
POST /purchase/marketplace-db with {item_id, value, seller_entity_id}

## 4) Founder can list payouts
GET /payouts/list?status=pending

## 5) Mark payout paid
POST /payouts/mark-paid?payout_id=...

## 6) Export payout report
GET /reports/payouts.csv
