from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.api.v1.health import router as health_router
from backend.common.constants import APP_NAME, APP_VERSION
from backend.config.logging import setup_logging
from backend.runtime.runtime import Runtime

setup_logging()

runtime = Runtime()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await runtime.start()
    yield
    await runtime.stop()


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    lifespan=lifespan,
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
        "status": runtime.state.value,
    }