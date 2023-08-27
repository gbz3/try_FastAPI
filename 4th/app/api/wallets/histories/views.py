from fastapi import APIRouter
from .schemas import History

router = APIRouter()

@router.get("/histories")
async def list_histories() -> list[History]:
    return [
        History(history_id=1),
        History(history_id=2),
    ]

@router.get("/histories/{history_id}")
async def get_history(history_id: int) -> History:
    return History(history_id=history_id)
