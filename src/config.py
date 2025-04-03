from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, EmailStr
from typing import Literal


class DBSettings(BaseModel):
    host: str
    port: int
    name: str
    user: str
    password: str

    @property
    def url(self) -> None:
        dbms = "postgresql"
        engine = "asyncpg"
        return f"{dbms}+{engine}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class OrganizationSettings(BaseModel):
    id: int
    name: str


class SMTPSettings(BaseModel):
    host: str
    port: int
    email: EmailStr
    password: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="CONFIG__",
    )
    mode: Literal["TEST", "LOCAL", "DEV", "PROD"]
    db: DBSettings
    organization: OrganizationSettings
    smtp: SMTPSettings


settings = Settings()
