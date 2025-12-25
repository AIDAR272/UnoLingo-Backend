from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.database.session import get_db

router = APIRouter(tags=["score"])


@router.get("/score")
def get_score(user_id : int, db : Session = Depends(get_db)):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    try:
        return user_service.get_user_score(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/score")
def increment_score(user_id, db : Session = Depends(get_db)):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    try:
        return user_service.increment_score(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
