from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import get_settings
from app.services.item_store import ItemStore


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        debug=settings.debug,
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url,
    )

    app.state.settings = settings
    app.state.item_store = ItemStore()
    app.state.item_store.seed_demo_items()

    app.include_router(api_router)
    return app


app = create_app()