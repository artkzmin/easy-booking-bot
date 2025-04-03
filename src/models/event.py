from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from src.models.base import BaseORM


class EventORM(BaseORM):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    datetime_start: Mapped[datetime]
    datetime_end: Mapped[datetime]
