from sqlalchemy import Column, DateTime, Integer, String
from datetime import datetime, timedelta, timezone
from database import Base


tzmsk = timezone(timedelta(hours=3))


class Complaint(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    status = Column(String, default="open")
    timestamp = Column(DateTime, default=datetime.now(tzmsk))
    sentiment = Column(String)
    category = Column(String, default="другое")
