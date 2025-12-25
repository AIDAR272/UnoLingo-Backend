from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreate, UserLogin
from app.services.user_service import UserService


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/sign-up")
def create_user(user : UserCreate, db : Session = Depends(get_db)):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    try:
        return user_service.sign_up(user_dto=user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/log-in")
def log_in(user : UserLogin, db : Session = Depends(get_db)):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    try:
        return user_service.log_in(user_dto=user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))