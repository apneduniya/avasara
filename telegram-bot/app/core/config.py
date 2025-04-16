import typing as t

from pydantic_settings import BaseSettings
from pydantic import field_validator


class Config(BaseSettings):
    # Application Configuration
    LOG_LEVEL: str = "INFO"
    ENVIRONMENT: str = "development"
    BOT_TOKEN: str
    LOGS_DIR: str = "logs"

    # Server Configuration
    API_URL: str = "http://localhost:8000/"

    # Frontend Configuration
    FRONTEND_URL: str = "http://localhost:3000"

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
