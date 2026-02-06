from fastapi import FastAPI

# Noetivis v13 consolidated build
from app.routers import attribution, auth, auth_db, auth_v2, batches_db, batching, content, contributors, creators, distribute, earnings, earnings_db, earnings_users, entities, intelligence, ledger, marketplace, monetization, payouts, payouts_db, purchase, purchase_attr, purchase_db, reports, safe_pay, treasury

app = FastAPI(title="Noetivis", version="13.0")

for _m in [attribution, auth, auth_db, auth_v2, batches_db, batching, content, contributors, creators, distribute, earnings, earnings_db, earnings_users, entities, intelligence, ledger, marketplace, monetization, payouts, payouts_db, purchase, purchase_attr, purchase_db, reports, safe_pay, treasury]:
    app.include_router(_m.router)

@app.get("/health")
def health():
    return {"status": "Noetivis v13 online", "routers": 26}
