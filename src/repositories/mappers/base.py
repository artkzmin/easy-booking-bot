from typing import TypeVar
from src.schemes import BaseDTO
from src.models import BaseORM


DBModelType = TypeVar("DBModelType", bound=BaseORM)
SchemaType = TypeVar("SchemaType", bound=BaseDTO)


class BaseDataMapper:
    db_model: type[DBModelType] = None
    schema: type[SchemaType] = None

    @classmethod
    def map_to_domain_entity(cls, db_model: BaseORM) -> BaseDTO:
        return cls.schema.model_validate(db_model, from_attributes=True)

    @classmethod
    def map_to_persistence_entity(cls, data: BaseDTO) -> BaseORM:
        return cls.db_model(data.model_dump())
