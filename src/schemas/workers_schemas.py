from pydantic import BaseModel
from typing import Optional
from schemas.vacancies_schemas import VacanciesGet


class WorkersGet(BaseModel):
    id: int 
    name: str
    surname: str
    resume: Optional[str]

    vacancies: list[VacanciesGet]


class WorkersAdd(BaseModel):
    name: str
    surname: str
    resume: Optional[str]

