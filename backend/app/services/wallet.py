
from sqlalchemy.orm import Session
from datetime import datetime
from app.models_phase20 import Wallet, WalletTxn

def get_wallet(db: Session, user_id: str, currency: str="USD") -> Wallet:
    w = db.query(Wallet).filter(Wallet.user_id==user_id, Wallet.currency==currency).first()
    if not w:
        w = Wallet(user_id=user_id, balance=0.0, currency=currency, updated_at=datetime.utcnow())
        db.add(w); db.commit(); db.refresh(w)
    return w

def credit(db: Session, wallet: Wallet, amount: float, provider: str, provider_ref: str, status: str="succeeded"):
    wallet.balance = float(wallet.balance) + float(amount)
    wallet.updated_at = datetime.utcnow()
    txn = WalletTxn(wallet_id=wallet.id, direction="credit", amount=float(amount), currency=wallet.currency,
                    provider=provider, provider_ref=provider_ref, status=status)
    db.add(txn); db.commit(); db.refresh(txn)
    return txn

def debit(db: Session, wallet: Wallet, amount: float, provider: str, provider_ref: str, status: str="succeeded"):
    wallet.balance = max(0.0, float(wallet.balance) - float(amount))
    wallet.updated_at = datetime.utcnow()
    txn = WalletTxn(wallet_id=wallet.id, direction="debit", amount=float(amount), currency=wallet.currency,
                    provider=provider, provider_ref=provider_ref, status=status)
    db.add(txn); db.commit(); db.refresh(txn)
    return txn
