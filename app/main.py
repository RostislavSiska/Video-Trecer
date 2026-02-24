"main"
from fastapi import FastAPI
from app.models import User, Movie, UserMovie 

app = FastAPI(title="Movie Tracker")

@app.get("/")
def root():
    """
    Да
    """
    return {"message": "Movie Tracker API"}
