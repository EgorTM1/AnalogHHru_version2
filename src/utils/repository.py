from abc import ABC, abstractmethod
from db.db import Session


class Abstract_repository(ABC):

    @abstractmethod
    async def add_one():
        raise NotImplemented
    

class Repository(Abstract_repository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with Session as session:
            add_obj = self.model(**data)

            session.add(add_obj)
            session.flush()
            await session.commit()

            return add_obj.id
