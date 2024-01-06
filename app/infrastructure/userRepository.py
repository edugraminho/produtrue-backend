from ..database.models import User
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id):
        user = self.db.query(User).filter(User.id == user_id).first()
        return user

    def save(self, user_data: dict) -> User:
        db_user = User(**user_data)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def update(self, user_data: dict, user_id:int) -> User:
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            for var, value in user_data.items():
                setattr(user, var, value)
            self.db.commit()
            self.db.refresh(user)
            return user
        return None # type: ignore
        
