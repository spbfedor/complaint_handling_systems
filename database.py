from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///complaints.db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class ComplaintsOrm(Model):
    __tablename__ = "complaints"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )
    text: Mapped[str]
    status: Mapped[str]
    timestamp: Mapped[str]
    sentiment: Mapped[str]
    category: Mapped[str]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def  delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)