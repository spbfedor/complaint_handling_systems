from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from contextlib import asynccontextmanager

from database import AsyncSessionLocal, create_tables
from crud import create_complaint
from schemas import ComplaintsCreate, ComplaintsResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    print("Завершение работы")


app = FastAPI(lifespan=lifespan)


async def get_db():
    async with AsyncSessionLocal() as db:
        yield db


@app.post("/complaint/", response_model=ComplaintsResponse)
async def post_complaint(
    complaint: ComplaintsCreate,
    db: AsyncSession = Depends(get_db)
):
    sentiment = ...
    category = ...

    db_complaint = await create_complaint(db, complaint)

    db_complaint.sentiment = sentiment
    db_complaint.category = category
    await db.commit()
    return db_complaint



