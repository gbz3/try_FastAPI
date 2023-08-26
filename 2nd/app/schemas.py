from pydantic import BaseModel

class Wallet(BaseModel):
    wallet_id: int
    name: str

class CreateWalletRequest(BaseModel):
    name: str
