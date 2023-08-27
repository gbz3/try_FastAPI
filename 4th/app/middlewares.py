from collections.abc import Callable
from datetime import datetime, timezone
from fastapi import FastAPI, Request, Response

def init_middlewares(app: FastAPI) -> None:
    @app.middleware("http")
    async def log_middleware(
        request: Request, call_next: Callable
    ) -> Response:
        st = datetime.now(tz=timezone.utc)
        response = await call_next(request)
        et = datetime.now(tz=timezone.utc)
        print(f"processing time: {et - st}")
        return response
