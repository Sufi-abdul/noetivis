
from celery import Celery

celery = Celery(
    "noetivis",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

celery.conf.timezone = "UTC"

celery.conf.beat_schedule = {
    "daily_payouts": {
        "task": "workers.tasks.run_daily_payouts",
        "schedule": 60 * 60 * 24,  # daily
    },
}
