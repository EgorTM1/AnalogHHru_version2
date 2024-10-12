from db.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import Optional

class VacanciesORM(Base):
    __tablename__ = 'vacancies'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str] = mapped_column(String(100))

    worker_id: Mapped[Optional[int]] = mapped_column(ForeignKey('workers.id'))

    worker: Mapped['WorkersORM'] = relationship(
        back_populates='vacancies'
    )
