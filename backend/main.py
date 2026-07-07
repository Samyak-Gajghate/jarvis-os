from fastapi import FastAPI

from backend.api.v1.health import router as health_router
from backend.common.constants import APP_NAME, APP_VERSION
from backend.config.logging import setup_logging

setup_logging()

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
)

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"],
)


@app.get("/")
async def root():
    return {
        "name": APP_NAME,
        "version": APP_VERSION,
        "status": "running",
    }