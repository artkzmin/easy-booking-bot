from enum import Enum
from src.schemes.base import BaseDTO


class UserRoleEnum(Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"


class UserDTO(BaseDTO):
    pass
