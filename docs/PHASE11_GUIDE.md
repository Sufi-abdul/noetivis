
# Phase 11 Guide

## Docker
1) Copy .env.example -> .env and edit values.
2) From repo root:
   docker compose -f deploy/docker-compose.yml up --build

API:
- http://localhost:8000/health

## API Keys
- Add keys in .env: NOETIVIS_API_KEYS=key1,key2
- Clients call with header: X-API-Key: key1

## Rate limiting
- Default 120 requests/minute per IP.
- Set NOETIVIS_RPM_LIMIT in .env.

## Audit logs
- audit.log is written in repo root by default.
- Set NOETIVIS_AUDIT_PATH to change location.

## CI
- GitHub Actions runs on push/PR and checks imports.
