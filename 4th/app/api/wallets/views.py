import asyncio
from fastapi import APIRouter, BackgroundTasks, Depends
from app.dependencies import APIKey
from app.exceptions import NotFound
from .schemas import ExportRequest, Wallet
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
async def get_wallet(
    wallet_id: int,
    api_key: APIKey,
) -> Wallet:
    if wallet_id == 0:
        raise NotFound(
            resource="Wallet", resource_id=wallet_id
        )
    return Wallet(wallet_id=wallet_id)

router.include_router(
    histories_router, prefix="/{wallet_id}"
)

async def export_wallets(dest: str) -> None:
    print(f"Exporting...")
    await asyncio.sleep(5)
    print(f"Completed: {dest}")

@router.post("/export", status_code=202)
async def export(
    data: ExportRequest,
    background_tasks: BackgroundTasks,
) -> None:
    background_tasks.add_task(
        export_wallets, data.dest
    )
