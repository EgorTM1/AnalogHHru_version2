from pydantic import BaseModel
from typing import Optional


class VacanciesAdd(BaseModel):
    title: str
    description: str

    worker_id: Optional[int] = None


class VacanciesGet(BaseModel):
    id: int
    title: str
    description: str

    worker_id: Optional[int]


class VacanciesAnswer(BaseModel):
    status: int
    detail: str
