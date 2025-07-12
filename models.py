from sqlalchemy import Column, DateTime, Integer, String
from datetime import datetime, timezone
from database import Base


tzmsk = timezone("Europe/Moscow")


class Complaint(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    status = Column(String, default="open")
    timestamp = Column(DateTime, default=datetime.now(tzmsk))
    sentiment = Column(String)
    category = Column(String, default="другое")
