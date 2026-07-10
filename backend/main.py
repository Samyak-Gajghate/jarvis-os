from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.api.v1.health import router as health_router
from backend.common.constants import APP_NAME, APP_VERSION
from backend.config.logging import setup_logging
from backend.container.dependencies import container
from backend.api.v1.models import router as model_router
from backend.api.v1.chat import router as chat_router
from backend.api.v1.planner import router as planner_router
from backend.api.v1.execute import router as execute_router
from backend.api.v1.research import router as research_router
from backend.api.v1.browser import router as browser_router
from backend.api.v1.search import router as search_router
from backend.api.v1.tools import (
    router as tools_router,
)


setup_logging()

runtime = container.resolve("runtime")


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

app.include_router(
    model_router,
    prefix="/api/v1/models",
    tags=["Models"],
)

app.include_router(
    chat_router,
    prefix="/api/v1/chat",
    tags=["Chat"],
)

app.include_router(
    planner_router,
    prefix="/api/v1/planner",
    tags=["Planner"],
)

app.include_router(
    execute_router,
    prefix="/api/v1/execute",
    tags=["Execution"],
)

app.include_router(
    research_router,
    prefix="/api/v1/research",
    tags=["Research"],
)
app.include_router(
    browser_router,
    prefix="/api/v1/browser",
    tags=["Browser"],
)
app.include_router(
    search_router,
    prefix="/api/v1/search",
    tags=["Search"],
)
app.include_router(
    tools_router,
    prefix="/api/v1/tools",
    tags=["Tools"],
)

@app.get("/")
async def root():
    return {
        "name": APP_NAME,
        "version": APP_VERSION,
        "status": runtime.state.value,
    }