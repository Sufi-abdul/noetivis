
from app.database import engine, Base
import app.models
import app.models_auth
import app.models_phase8
import app.models_phase10
import app.models_phase18
import app.models_phase19

def init():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()
