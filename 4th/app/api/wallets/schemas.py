from pydantic import BaseModel

class Wallet(BaseModel):
    wallet_id: int

class ExportRequest(BaseModel):
    dest: str
