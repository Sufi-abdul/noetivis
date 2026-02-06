
from sqlalchemy.orm import Session
from app.models_phase10 import ContributorAllocation
from app.models_phase8 import Payout
from app.services.treasury import get_pool, deduct_from_pool

def list_contributors(db: Session):
    return db.query(ContributorAllocation).filter(ContributorAllocation.active==True).all()

def distribute_contributor_pool(db: Session, currency: str="USD"):
    pool = get_pool(db, "contributors_pool", currency)
    total_pool = float(pool.amount)
    if total_pool <= 0:
        return {"distributed": False, "reason": "pool_empty"}

    contributors = list_contributors(db)
    if not contributors:
        return {"distributed": False, "reason": "no_contributors"}

    total_weight = sum(float(c.weight) for c in contributors) or 1.0
    created = []
    for c in contributors:
        share = total_pool * (float(c.weight) / total_weight)
        # Create payout row assigned to contributor_user_id
        p = Payout(ledger_id="POOL", payee_role="contributor", payee_user_id=c.contributor_user_id,
                  amount=share, currency=currency, status="pending")
        db.add(p)
        created.append({"contributor_user_id": c.contributor_user_id, "amount": round(share,6)})
    db.commit()

    # Deduct from pool after creating payouts
    deduct_from_pool(db, "contributors_pool", total_pool, currency)
    return {"distributed": True, "total": round(total_pool,6), "created": created}
