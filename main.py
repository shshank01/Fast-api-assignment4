from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

movies = [
    {
        "id": 1,
        "title": "3 Idiots",
        "director": "Rajkumar Hirani",
        "genre": "Comedy Drama",
        "language": "Hindi",
        "release_year": 2009,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Baahubali",
        "director": "S S Rajamouli",
        "genre": "Action Drama",
        "language": "Telugu",
        "release_year": 2015,
        "is_available": True
    }
]


class MovieUpdate(BaseModel):
    title: str
    director: str
    genre: str
    language: str
    release_year: int
    is_available: bool


@app.get("/")
def home():
    return {"message": "Welcome to Movies API"}


@app.get("/movies")
def get_movies():
    return movies


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie: MovieUpdate):
    for existing_movie in movies:
        if existing_movie["id"] == movie_id:
            existing_movie["title"] = movie.title
            existing_movie["director"] = movie.director
            existing_movie["genre"] = movie.genre
            existing_movie["language"] = movie.language
            existing_movie["release_year"] = movie.release_year
            existing_movie["is_available"] = movie.is_available

            return {
                "message": "Movie updated successfully",
                "movie": existing_movie
            }

    raise HTTPException(status_code=404, detail="Movie not found")