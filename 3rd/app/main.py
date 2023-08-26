from httpx import AsyncClient
from fastapi import FastAPI

BASE_URL = "https://api.github.com"
app = FastAPI()

@app.get("/awesome_orgs")
async def get_awesome_orgs() -> list[int]:
    async with AsyncClient(base_url=BASE_URL) as c:
        print("started: 1")
        api_1 = await c.get("/orgs/python")
        print("started: 2")
        api_2 = await c.get("/orgs/pydantic")
        print("started: 3")
        api_3 = await c.get("/orgs/encode")
        print("finished")
    result = [
        api_1.status_code,
        api_2.status_code,
        api_3.status_code,
    ]
    return result

@app.get("/async_hello")
async def get_async_hello():
    return {"hello": "world"}
