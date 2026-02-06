
from app.database import engine, Base
import models
import models_auth  # ensures AuthUser is registered

def init():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()
