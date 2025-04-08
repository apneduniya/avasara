from pydantic_settings import BaseSettings
from pydantic import field_validator


class Config(BaseSettings):
    # Basic details
    PROJECT_NAME: str = "Avasara"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "AI-powered real-time opportunity aggregator that gathers opportunities from various platforms and matches them to users based on their skills and profiles."

    # Application Configuration
    LOG_LEVEL: str = "INFO"
    ENVIRONMENT: str = "development"
    LOGS_DIR: str = "logs"

    # Frontend Configuration
    FRONTEND_URL: str

    # APScheduler Configuration
    APSCHEDULER_RUN_ON_STARTUP: bool = False # Run immediately once on startup (Default: False)

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