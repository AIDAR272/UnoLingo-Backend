from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True , nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    score = Column(Integer, default=0)

    translations = relationship("Translation", back_populates="user")


class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    word = Column(String(255), nullable=False)
    translation = Column(String(255), nullable=False)

    user = relationship("User", back_populates="translations")