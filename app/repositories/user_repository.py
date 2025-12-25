from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:
    def __init__(self, db : Session):
        self.db = db

    def get_user_by_username(self, username : str):
        return self.db.query(User).filter(User.username == username).first()

    def create_user(self, username, hashed_password):
        user = User(username=username, hashed_password=hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_score(self, user_id):
        user_instance = self.db.query(User).filter(User.id == user_id).first()
        if not user_instance:
            raise HTTPException(status_code=404, detail="User not found")
        return user_instance.score

    def increment_score(self, user_id):
        user_instance = self.db.query(User).filter(User.id == user_id).first()
        if not user_instance:
            raise HTTPException(status_code=404, detail="User not found")
        user_instance.score += 1
        self.db.commit()
