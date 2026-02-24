"main"
from fastapi import FastAPI
from app.database import engine, Base
from app.models import User, Movie, UserMovie 

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Tracker")

@app.get("/")
def root():
    """
    Да
    """
    return {"message": "Movie Tracker API"}
