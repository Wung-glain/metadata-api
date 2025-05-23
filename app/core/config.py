from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str  # Add this line

    class Config:
        env_file = ".env"


settings = Settings()
