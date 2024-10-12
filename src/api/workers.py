from fastapi import APIRouter
from services.workers_service import WorkersService
from schemas.workers_schemas import WorkersAdd, WorkersGet


router_workers = APIRouter(
    prefix='/workers',
    tags=['Workers']
)


@router_workers.post('')
async def add_worker(data: WorkersAdd) -> int:
    res = await WorkersService().add_worker(data)

    return res


@router_workers.get('')
async def get_all() -> list[WorkersGet]:
    res = await WorkersService().get_all()

    return res
