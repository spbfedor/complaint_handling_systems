from pydantic import BaseModel
from datetime import datetime


class ComplaintsCreate(BaseModel):
    text: str


class ComplaintsResponse(BaseModel):
    id: int
    text: str
    status: str
    timestamp: datetime
    sentiment: str
    category: str
