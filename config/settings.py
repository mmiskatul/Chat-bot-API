# Use pydantic-settings instead of pydantic
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_name: str = "Qwen/Qwen3-0.6B"
    device: int = -1  # 0 = GPU, -1 = CPU
    max_new_tokens: int = 200
    temperature: float = 0.7

    class Config:
        env_file = ".env"  # optional: read from .env

settings = Settings()
