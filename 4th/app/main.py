from fastapi import FastAPI
from .api import router as api_router
from .exceptions import init_exception_handler
from .middlewares import init_middlewares

app = FastAPI()
init_exception_handler(app)
init_middlewares(app)
app.include_router(api_router, prefix="/api")
