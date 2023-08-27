from contextlib import asynccontextmanager
from fastapi import FastAPI
from .api import router as api_router
from .exceptions import init_exception_handler
from .middlewares import init_middlewares

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("startup!!!")
    yield
    print("shutdown!!!")

app = FastAPI(lifespan=lifespan)
init_exception_handler(app)
init_middlewares(app)
app.include_router(api_router, prefix="/api")
