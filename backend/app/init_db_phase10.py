
from app.database import engine, Base
import models
import models_auth
import models_phase8
import models_phase10

def init():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()
