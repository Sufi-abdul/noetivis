
# Phase 9 Guide

## Goal
Make payouts point to the correct people automatically using Attribution mapping.

## Steps
1) Apply Phase 9 overlay
2) Ensure Phase 8 init DB has been run already.
3) Set attribution for seller entity:
POST /attribution/set
  subject_type: "entity"
  subject_id: "<seller_entity_id>"
  owner_user_id: "<owner_auth_user_id>"
  partner_user_id: "<partner_auth_user_id>"
  reseller_user_id: "<reseller_auth_user_id>" (optional)

4) Run purchase:
POST /purchase/marketplace-attr
This will:
- write ledger row
- create payouts with payee_user_id for owner/partner/reseller

5) Users check earnings:
GET /earnings/me (Bearer token)

6) Founder batching:
POST /batch/create
GET /batch/receipt?role=partner&payee_user_id=<id>
