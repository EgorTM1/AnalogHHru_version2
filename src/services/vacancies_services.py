from utils.repository import Repository
from db.db import Session
from models.vacancy_model import VacanciesORM
from schemas.vacancies_schemas import VacanciesAdd, VacanciesAnswer


class VacanciesRepository(Repository):
    model = VacanciesORM

    async def add_vacancies(self, data: VacanciesAdd) -> int:
        info_vacancies = data.model_dump()

        res = await super().add_one(info_vacancies)

        return res
    

    async def update_vakancies(self, vacancy_id: int, new_worker_id: int) -> VacanciesAnswer:
        async with Session as session:
            try:
                vacancy = await session.get(VacanciesORM, vacancy_id)
                vacancy.worker_id = new_worker_id

                await session.commit()

                return {'status': 200, 'detail': 'Success!'}

            except Exception:
                raise {'status': 404, 'detail': 'something went wrong!'}
