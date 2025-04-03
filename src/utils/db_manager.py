class DBManager:
    def __init__(self, session_factory) -> None:
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

    async def __aexit__(self, *args) -> None:
        await self.session.rollback()
        await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()
