from fastapi import APIRouter

router = APIRouter(prefix="/v1/wallets")

@router.get("")
async def get_wallets():
    """Walletの一覧取得API"""
    return {"wallets": []}
