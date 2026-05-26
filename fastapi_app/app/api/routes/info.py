from fastapi import APIRouter, Request


router = APIRouter(tags=["Info"])


def _settings_payload(request: Request) -> dict[str, str | bool]:
    settings = request.app.state.settings
    return settings.as_dict()


@router.get("/")
def root(request: Request) -> dict[str, str | bool | dict[str, str]]:
    settings = _settings_payload(request)
    return {
        "message": "FastAPI project is running",
        "environment": settings["environment"],
        "docs": settings["docs_url"],
        "redoc": settings["redoc_url"],
        "status": "/health",
    }


@router.get("/info")
def info(request: Request) -> dict[str, str | bool]:
    return _settings_payload(request)