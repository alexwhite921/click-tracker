from .database import engine
from models.click import Click
from db.database import Base

def init_db():
    Base.metadata.create_all(bind=engine)
