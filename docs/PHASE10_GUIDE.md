
# Phase 10 Guide

## 1) Create tables (Phase 1–10)
python backend/app/init_db_phase10.py

## 2) Treasury pools
- founder_pool
- contributors_pool
- ops_pool

Add to contributors pool:
POST /treasury/add?pool=contributors_pool&amount=100

## 3) Register contributors (weights)
POST /contributors/set
{
  "contributor_user_id": "<auth_user_id>",
  "weight": 2.0,
  "active": true
}

## 4) Distribute contributor pool into payout rows
POST /distribute/contributors
This will create payouts with payee_role="contributor" and deduct the pool to 0.

## 5) Safe payment (anti-dup)
POST /safe/mark-paid?payout_id=...
Locks payout_id to prevent double marking paid.
