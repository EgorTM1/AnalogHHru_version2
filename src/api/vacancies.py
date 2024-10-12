from fastapi import APIRouter
from services.vacancies_services import VacanciesRepository
from schemas.vacancies_schemas import VacanciesAdd, VacanciesAnswer


router_vacancies = APIRouter(
    prefix='/vacancies',
    tags=['Vacancies']
)


@router_vacancies.post('')
async def add_vacancies(data: VacanciesAdd) -> int:
    res = await VacanciesRepository().add_vacancies(data)

    return res


@router_vacancies.put('/{vacancy_id}')
async def update_vacancies(vacancy_id: int, new_worker_id: int) -> VacanciesAnswer:
    res = await VacanciesRepository().update_vakancies(vacancy_id, new_worker_id)

    return res
