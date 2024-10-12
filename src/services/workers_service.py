from db.db import Session
from utils.repository import Repository
from models.worker_model import WorkersORM
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from schemas.workers_schemas import WorkersAdd, WorkersGet


class WorkersService(Repository):
    model = WorkersORM

    async def add_worker(self, data: WorkersAdd) -> int:
        info_worker = data.model_dump()

        res = await super().add_one(info_worker)

        return res
        

    async def get_all(self) -> list[WorkersGet]:
        async with Session as session:
            query = (
                select(self.model)
                .options(selectinload(self.model.vacancies))
            )

            res = await session.execute(query)
            result = [WorkersGet.model_validate(row, from_attributes=True) for row in res.scalars().all()]

            return result 
    