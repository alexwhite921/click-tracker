from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = 'postgresql://postgres:qcgZtqenHndhcBlAJWxyxqJeBkKBGOhA@shuttle.proxy.rlwy.net:58997/railway'
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
