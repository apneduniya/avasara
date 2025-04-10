import typing as t

from pydantic_settings import BaseSettings
from pydantic import field_validator


class Config(BaseSettings):
    # Application Configuration
    LOG_LEVEL: t.Optional[str] = "INFO"
    ENVIRONMENT: t.Optional[str] = "development"
    BOT_TOKEN: str
    LOGS_DIR: t.Optional[str] = "logs"

    # Server Configuration
    API_URL: t.Optional[str] = "http://localhost:8000/"

    # Database Configuration
    POSTGRES_USER: t.Optional[str] = "postgres"
    POSTGRES_PASSWORD: t.Optional[str] = "postgres"
    POSTGRES_DB: t.Optional[str] = "avasara"
    POSTGRES_HOST: t.Optional[str] = "localhost"
    POSTGRES_PORT: t.Optional[str] = "5432"
    DATABASE_URL: t.Optional[str] = None
    ASYNC_DATABASE_URL: t.Optional[str] = None

    def get_database_url(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    def get_async_database_url(self) -> str:
        if self.ASYNC_DATABASE_URL:
            return self.ASYNC_DATABASE_URL
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        env_file = ".env"
        case_sensitive = True

    @field_validator("LOG_LEVEL")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        """Validate that log level is a valid logging level."""
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        v = v.upper()
        if v not in valid_levels:
            raise ValueError(f"Log level must be one of {valid_levels}")
        return v


config = Config()
