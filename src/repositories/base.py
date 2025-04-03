from src.schemes.base import BaseDTO
from src.models import BaseORM
from src.repositories.mappers import BaseDataMapper


class BaseRepository:
    model: BaseORM | None = None
    mapper: BaseDataMapper | None = None

    def __init__(self, session) -> None:
        self.session = session

    async def get_filtered(self) -> BaseDTO:
        pass

    async def add(self) -> int:
        pass

    async def delete(self) -> None:
        pass

    async def edit(self) -> None:
        pass
