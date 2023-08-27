from fastapi import APIRouter, HTTPException
from .schemas import Wallet
from .histories.views import (
    router as histories_router,
)

router = APIRouter(prefix="/wallets")

@router.get("")
async def list_wallets() -> list[Wallet]:
    return [
        Wallet(wallet_id=1),
        Wallet(wallet_id=2),
    ]

@router.get("/{wallet_id}")
async def get_wallet(wallet_id: int) -> Wallet:
    if wallet_id == 0:
        raise HTTPException(status_code=404)
    return Wallet(wallet_id=wallet_id)

router.include_router(
    histories_router, prefix="/{wallet_id}"
)
