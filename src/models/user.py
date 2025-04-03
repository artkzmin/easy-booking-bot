from sqlalchemy.orm import mapped_column, Mapped
from src.models.base import BaseORM
from src.schemes import UserRoleEnum


class UserORM(BaseORM):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname: Mapped[str]
    role: Mapped[UserRoleEnum] = mapped_column(default=UserRoleEnum.CUSTOMER)
