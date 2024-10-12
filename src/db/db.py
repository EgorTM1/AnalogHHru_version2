from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config import settings


engine = create_async_engine(
    url=settings.DB_URL,
    echo=True
)
session_maker = async_sessionmaker(engine, expire_on_commit=False)

Session = session_maker()


class Base(DeclarativeBase):
    pass
