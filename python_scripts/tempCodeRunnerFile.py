from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Movie(BaseModel):
    id: str
    title: str
    posterUrl: str
    synopsis: str
    genres: List[str]
    rating: float

app = FastAPI()

@app.get("/movies", response_model=List[Movie])
async def get_movies():
    return [
        {
            "id": "1",
            "title": "Inception",
            "posterUrl": "https://image.tmdb.org/t/p/w500/tWqifoYuwLETmmasnGHO7xBjEtt.jpg",
            "synopsis": "A thief who steals corporate secrets through the use of dream-sharing technology.",
            "genres": ["Action", "Sci-Fi"],
            "rating": 8.8
        },
        {
            "id": "2",
            "title": "The Matrix",
            "posterUrl": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
            "synopsis": "A computer hacker learns about the true nature of his reality.",
            "genres": ["Action", "Sci-Fi"],
            "rating": 8.7
        }
        # Add as many movies as you like
    ]
