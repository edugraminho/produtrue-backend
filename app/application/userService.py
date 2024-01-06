from ..database.models import User
from ..infrastructure.userRepository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_tweet(self, user_id, q):
        return self.user_repository.get_user(user_id)

    def create_user(self, user_data: dict) -> User:
        return self.user_repository.save(user_data)

    def update_user(self, user_data: dict, user_id: int) -> User:
        return self.user_repository.update(user_data, user_id)
