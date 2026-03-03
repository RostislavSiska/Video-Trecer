"main"
from fastapi import FastAPI, Depends, HTTPException
from app.schemas import UserCreate
from app.models import User, Movie, UserMovie
from app.database import get_db
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import psycopg2
from sqlalchemy import text
from fastapi import FastAPI
from app.database import engine
from app.database import Base
from app.routers import auth


app = FastAPI(title="Movie Tracker")



@app.get("/")
def root():
    """
    Да
    """
    return {"message": "Movie Tracker API"}

@app.get("/user/")
def read_users(db: Session = Depends(get_db)):
    """
    Полчуние всех записей
    """
    return db.execute(select(User)).scalars().all()


@app.post("/user/add")
def add_users(user: UserCreate, db: Session = Depends(get_db)):
    """
    Добавление полльзователя
    """
    usbd = User(username = user.username, email = user.email, hashed_password = user.password)
    try:
        db.add(usbd)
        db.commit()
        db.refresh(usbd)
        return user
    except(IntegrityError, psycopg2.errors.UniqueViolation):
        db.rollback()
        return {"message": "Уже есть"}

app.include_router(auth.router)
# другие роутеры пока не подключены