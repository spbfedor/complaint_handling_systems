from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from models import Complaint
from schemas import ComplaintsCreate, ComplaintsResponse


async def create_complaint(db: AsyncSession, complaint: ComplaintsCreate):
    db_complaint = Complaint(text=complaint.text)
    db.add(db_complaint)
    await db.commit()
    await db.refresh(db_complaint)
    return db_complaint


async def get_complaint(db: AsyncSession, complaint_id: int):
    result = await db.get(Complaint, complaint_id)
    if not result:
        raise HTTPException(status_code=404, detail="Complaint not found")
    return result