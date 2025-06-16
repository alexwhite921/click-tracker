from sqlalchemy import Column, Integer, String, DateTime, func
from db.database import Base

class Click(Base):
    __tablename__ = "clicks"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    ip = Column(String, nullable=False)
    user_agent = Column(String, nullable=False)
    referrer = Column(String)
    source = Column(String)
    campaign = Column(String)
