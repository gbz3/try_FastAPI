import pytest

@pytest.mark.anyio
async def test_get_async_hello(ac):
    response = await ac.get("/async_hello")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}
