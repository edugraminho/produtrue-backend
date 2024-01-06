# tests/test_user.py
import pytest
from httpx import AsyncClient
from app.api import app  # adjust the import path according to your project structure


@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.post(
            "/users/", json={"username": "testuser", "email": "test@example.com"}
        )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"


@pytest.mark.asyncio
async def test_read_user():
    user_id = 1  # assuming there is already a user with id 1
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id


@pytest.mark.asyncio
async def test_update_user():
    user_id = 1  # assuming there is already a user with id 1
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.put(
            f"/users/{user_id}",
            json={"username": "updateduser", "email": "updated@example.com"},
        )
    assert response.status_code == 200
    assert response.json()["username"] == "updateduser"


@pytest.mark.asyncio
async def test_delete_user():
    user_id = 1  # assuming there is already a user with id 1
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "User deleted successfully"
