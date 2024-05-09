from src.main import app as fastapi_app
from httpx import AsyncClient
import pytest
import json
import asyncio
import sys
from os.path import abspath, dirname

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))


def open_mock_json(model: str):
    with open(f"src/tests/mock_{model}.json", encoding="utf-8") as file:
        return json.load(file)


@pytest.mark.asyncio(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac
