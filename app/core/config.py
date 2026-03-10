"config"
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Настройки config
    """
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    TMDB_API_KEY: Optional[str] = None
    TMDB_ACCESS_TOKEN: Optional[str] = None
    TMDB_BASE_URL: str = "https://proxyservicetmdb.onrender.com/TMDBProxy"
    TMDB_IMAGE_BASE_URL: str = "https://proxyservicetmdb.onrender.com/TMDBProxy/images"

    class Config:
        """
        config
        """
        env_file = ".env"

settings = Settings()
