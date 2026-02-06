# Noetivis v13 Quickstart

## Local API
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Docker
```bash
cp .env.example .env
docker compose -f deploy/docker-compose.yml up --build
```

- API health: http://localhost:8000/health
- Landing page: open landing/index.html
