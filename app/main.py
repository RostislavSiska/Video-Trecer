"main"
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import psycopg2
from sqlalchemy import text
from fastapi import FastAPI
from app.routers import auth, movies


app = FastAPI(title="Movie Tracker")



@app.get("/")
def root():
    """
    Да
    """
    return {"message": "Movie Tracker API"}

app.include_router(auth.router)
app.include_router(movies.router)
