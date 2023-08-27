from fastapi import APIRouter
from .histories.views import router as histories_router

router = APIRouter()
router.include_router(histories_router)
