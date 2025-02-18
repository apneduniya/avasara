from pydantic_settings import BaseSettings


class Config(BaseSettings):
    # Application Configuration
    LOG_LEVEL: str = "INFO"
    ENVIRONMENT: str = "development"
    BOT_TOKEN: str
    LOGS_DIR: str = "logs"

    # Server Configuration
    API_URL: str = "http://localhost:8000/"

    class Config:
        env_file = ".env"


config = Config() 