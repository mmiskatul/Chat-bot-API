from pydantic import BaseSettings

class Settings(BaseSettings):
    model_name: str = "Qwen/Qwen3-0.6B"
    device: int = 0  # 0 for GPU, -1 for CPU
    max_new_tokens: int = 200
    temperature: float = 0.7

    class Config:
        env_file = ".env"

settings = Settings()
