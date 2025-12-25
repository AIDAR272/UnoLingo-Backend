import random
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User, Translation
from app.services.translate_service import translate

router = APIRouter()

@router.get("/translate")
def translate_word(word: str):
    return {"message": translate(word, "ru")}


@router.get("/word")
def get_word(user_id : int, db : Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_translations = user.translations
    word = random.choice(user_translations)
    return word


@router.post("/word")
def add_word(user_id : int, word : str, translation : str, db : Session = Depends(get_db)):
    db.add(Translation(word=word, user_id=user_id, translation=translation))
    db.commit()
    return {"message": "Word added successfully"}