from db.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional


class WorkersORM(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname: Mapped[str]
    resume: Mapped[Optional[str]]

    vacancies: Mapped[list['VacanciesORM']] = relationship(
        back_populates='worker'
    )
