import asyncio
from datetime import datetime
import httpx

async def get(id_: int, url: str) -> str:
    st = datetime.now()
    async with httpx.AsyncClient() as ac:
        print(f"{id_} started")
        res = await ac.get(url)
        print(f"{id_} finished: {datetime.now() - st}")
    return f"{id_}:{res.status_code}"

async def main():
    print(f"main started")
    st = datetime.now()
    base_url = "https://api.github.com"
    result = await asyncio.gather(
        get(1, f"{base_url}/orgs/python"),
        get(2, f"{base_url}/orgs/pydantic"),
        get(3, f"{base_url}/orgs/encode"),
    )
    print(f"{result=}")
    print(f"main finished: {datetime.now() - st}")

if __name__ == "__main__":
    asyncio.run(main())
