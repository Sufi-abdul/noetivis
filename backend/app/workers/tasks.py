
from app.workers.celery_app import celery

@celery.task(name="workers.tasks.run_daily_payouts")
def run_daily_payouts():
    # In production: query ledger, generate payouts, mark paid, export reports
    return {"status": "daily payouts stub executed"}
