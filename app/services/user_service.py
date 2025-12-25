from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreate, UserLogin, UserResponse
from app.core.security import hash_password, verify_password, create_access_token


class UserService:
    def __init__(self, user_repository : UserRepository):
        self.user_repository = user_repository


    def sign_up(self, user_dto : UserCreate):
        user = self.user_repository.get_user_by_username(user_dto.username)
        if user is not None:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )

        hashed_password = hash_password(user_dto.password)
        new_user = self.user_repository.create_user(user_dto.username, hashed_password)

        token = create_access_token({"sub" : user_dto.username})
        return UserResponse(id=new_user.id, token=token)


    def log_in(self, user_dto : UserLogin):
        user = self.user_repository.get_user_by_username(user_dto.username)
        if user is None:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Username is not registered or not correct"
            )

        if not verify_password(user_dto.password, user.hashed_password):
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Password is incorrect"
            )

        token = create_access_token({"sub":user_dto.username})
        return UserResponse(id=user.id, token=token)


    def get_user_score(self, user_id):
        return self.user_repository.get_user_score(user_id)

    def increment_score(self, user_id):
        return self.user_repository.increment_score(user_id)