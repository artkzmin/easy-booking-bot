from src.schemes.base import BaseDTO


class BaseRepository:
    async def get(self) -> BaseDTO:
        pass

    async def add(self) -> int:
        pass

    async def delete(self) -> None:
        pass

    async def edit(self) -> None:
        pass
