from typing import Annotated
from fastapi import (Depends, HTTPException, Security, status)
from fastapi.security import APIKeyHeader

async def get_api_key(
    api_key_header: str = Security(
        APIKeyHeader(
            name="APP-API-KEY", auto_error=True
        )
    ),
) -> str:
    if api_key_header != "DUMMY-KEY":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
    return api_key_header

APIKey = Annotated[str, Depends(get_api_key)]
