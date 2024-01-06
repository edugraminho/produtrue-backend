# tests/test_integration.py
import pytest
from httpx import AsyncClient
from app.api import app  # adjust the import path according to your project structure


@pytest.mark.asyncio
async def test_user_tweet_flow():
    # Create a user
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        user_response = await ac.post(
            "/users/",
            json={"username": "integration_test", "email": "integration@test.com"},
        )
        user_id = user_response.json()["id"]

    # Create a tweet for the user
    tweet_response = await ac.post(
        "/tweets/", json={"content": "Integration test tweet", "author_id": user_id}
    )
    tweet_id = tweet_response.json()["id"]

    # Read the tweet
    read_tweet_response = await ac.get(f"/tweets/{tweet_id}")
    assert read_tweet_response.json()["content"] == "Integration test tweet"

    # Delete the tweet
    delete_tweet_response = await ac.delete(f"/tweets/{tweet_id}")
    assert delete_tweet_response.json()["detail"] == "Tweet deleted successfully"

    # Delete the user
    delete_user_response = await ac.delete(f"/users/{user_id}")
    assert delete_user_response.json()["detail"] == "User deleted successfully"
