from sqlalchemy.orm import mapped_column, Mapped
from src.models.base import BaseOrm
from src.schemes import UserRoleEnum


class UserORM(BaseOrm):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname: Mapped[str]
    role: Mapped[UserRoleEnum]
