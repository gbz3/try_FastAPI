from fastapi import FastAPI
from .api import router as api_router
from .exceptions import init_exception_handler

app = FastAPI()
init_exception_handler(app)
app.include_router(api_router, prefix="/api")

