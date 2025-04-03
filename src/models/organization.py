from sqlalchemy.orm import Mapped, mapped_column
from src.models.base import BaseORM


class OrganizationORM(BaseORM):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
