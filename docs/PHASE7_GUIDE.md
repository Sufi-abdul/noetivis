
# Phase 7 Guide

## 1) Create DB tables
Run:
python backend/app/init_db_phase7.py

## 2) Sign up a DB user
POST /auth/signup-db with {email, password, role}

## 3) Login
POST /auth/login-db -> returns JWT

## 4) Use token
Authorization: Bearer <token>

## 5) Earnings summary (MVP)
POST /earnings/summary with ledger events list
(Phase 8 will wire this to ledger DB rows and user/entity mapping)

## 6) Scheduled payouts
Celery + Redis stubs included. In production, use beat schedule (weekly/monthly).
