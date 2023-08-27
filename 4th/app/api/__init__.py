from fastapi import APIRouter
from .wallets.views import router as wallets_router

router = APIRouter()
router.include_router(wallets_router)
