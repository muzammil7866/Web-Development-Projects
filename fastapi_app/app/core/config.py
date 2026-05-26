from functools import lru_cache
import os


class Settings:
    def __init__(self) -> None:
        self.app_name = os.getenv("APP_NAME", "FastAPI Project Hub")
        self.version = os.getenv("APP_VERSION", "1.0.0")
        self.environment = os.getenv("APP_ENV", "development")
        self.debug = os.getenv("FASTAPI_DEBUG", "true").lower() in {"1", "true", "yes", "on"}
        self.docs_url = os.getenv("DOCS_URL", "/docs")
        self.redoc_url = os.getenv("REDOC_URL", "/redoc")

    def as_dict(self) -> dict[str, str | bool]:
        return {
            "app_name": self.app_name,
            "version": self.version,
            "environment": self.environment,
            "debug": self.debug,
            "docs_url": self.docs_url,
            "redoc_url": self.redoc_url,
        }


@lru_cache
def get_settings() -> Settings:
    return Settings()