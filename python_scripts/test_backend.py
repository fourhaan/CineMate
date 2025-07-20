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
        },
        {
            "id": "3",
            "title": "Interstellar",
            "posterUrl": "https://image.tmdb.org/t/p/w500/rAiYTfKGqDCRIIqo664sY9XZIvQ.jpg",
            "synopsis": "A team of explorers travel through a wormhole in space.",
            "genres": ["Adventure", "Drama", "Sci-Fi"],
            "rating": 8.6
        },
        {
            "id": "4",
            "title": "The Dark Knight",
            "posterUrl": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
            "synopsis": "Batman confronts the Joker, a criminal mastermind.",
            "genres": ["Action", "Crime", "Drama"],
            "rating": 9.0
        },
        {
            "id": "5",
            "title": "Forrest Gump",
            "posterUrl": "https://image.tmdb.org/t/p/w500/saHP97rTPS5eLmrLQEcANmKrsFl.jpg",
            "synopsis": "The presidencies of Kennedy and Johnson, the Vietnam War, and Watergate from the perspective of an Alabama man.",
            "genres": ["Drama", "Romance"],
            "rating": 8.8
        },
        {
            "id": "6",
            "title": "Pulp Fiction",
            "posterUrl": "https://image.tmdb.org/t/p/w500/dM2w364MScsjFf8pfMbaWUcWrR.jpg",
            "synopsis": "The lives of two mob hitmen, a boxer, and others intertwine in four tales of violence and redemption.",
            "genres": ["Crime", "Drama"],
            "rating": 8.9
        },
        {
            "id": "7",
            "title": "Fight Club",
            "posterUrl": "https://image.tmdb.org/t/p/w500/bptfVGEQuv6vDTIMVCHjJ9Dz8PX.jpg",
            "synopsis": "An insomniac office worker and a soap maker form an underground fight club.",
            "genres": ["Drama"],
            "rating": 8.8
        },
        {
            "id": "8",
            "title": "The Lord of the Rings: The Fellowship of the Ring",
            "posterUrl": "https://image.tmdb.org/t/p/w500/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg",
            "synopsis": "A meek Hobbit and eight companions set out on a journey to destroy the One Ring.",
            "genres": ["Adventure", "Drama", "Fantasy"],
            "rating": 8.8
        },
        {
            "id": "9",
            "title": "The Lord of the Rings: The Two Towers",
            "posterUrl": "https://image.tmdb.org/t/p/w500/5VTN0pR8gcqV3EPUHHfMGnJYN9L.jpg",
            "synopsis": "While Frodo and Sam edge closer to Mordor, the divided fellowship makes a stand against Sauron's new ally.",
            "genres": ["Adventure", "Drama", "Fantasy"],
            "rating": 8.7
        },
        {
            "id": "10",
            "title": "The Lord of the Rings: The Return of the King",
            "posterUrl": "https://image.tmdb.org/t/p/w500/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg",
            "synopsis": "Gandalf and Aragorn lead the World of Men against Sauron's army.",
            "genres": ["Adventure", "Drama", "Fantasy"],
            "rating": 8.9
        },
        {
            "id": "11",
            "title": "The Shawshank Redemption",
            "posterUrl": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
            "synopsis": "Two imprisoned men bond over a number of years, finding solace and eventual redemption.",
            "genres": ["Drama"],
            "rating": 9.3
        },
        {
            "id": "12",
            "title": "The Godfather",
            "posterUrl": "https://image.tmdb.org/t/p/w500/eEslKSwcqmiNS6va24Pbxf2UKmJ.jpg",
            "synopsis": "The aging patriarch of an organized crime dynasty transfers control to his reluctant son.",
            "genres": ["Crime", "Drama"],
            "rating": 9.2
        },
        {
            "id": "13",
            "title": "The Godfather: Part II",
            "posterUrl": "https://image.tmdb.org/t/p/w500/bVq65huQ8vHDd1a4Z37QtuyEvpA.jpg",
            "synopsis": "The early life and career of Vito Corleone in 1920s New York.",
            "genres": ["Crime", "Drama"],
            "rating": 9.0
        },
        {
            "id": "14",
            "title": "The Avengers",
            "posterUrl": "https://image.tmdb.org/t/p/w500/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg",
            "synopsis": "Earth's mightiest heroes must come together to save the world.",
            "genres": ["Action", "Science Fiction", "Adventure"],
            "rating": 8.0
        },
        {
            "id": "15",
            "title": "Avengers: Endgame",
            "posterUrl": "https://image.tmdb.org/t/p/w500/ulzhLuWrPK07P1YkdWQLZnQh1JL.jpg",
            "synopsis": "After the devastating events, the universe is in ruins. The Avengers assemble once more.",
            "genres": ["Action", "Adventure", "Science Fiction"],
            "rating": 8.4
        },
        {
            "id": "16",
            "title": "Avatar",
            "posterUrl": "https://image.tmdb.org/t/p/w500/kmcqlZGaSh20zpTbuoF0Cdn07dT.jpg",
            "synopsis": "A paraplegic Marine dispatched to the moon Pandora.",
            "genres": ["Action", "Adventure", "Fantasy"],
            "rating": 7.8
        },
        {
            "id": "17",
            "title": "Jurassic Park",
            "posterUrl": "https://image.tmdb.org/t/p/w500/c414cDeQ9b6qLPLeKmiJuLDUREJ.jpg",
            "synopsis": "During a preview tour, a theme park suffers a major power breakdown.",
            "genres": ["Adventure", "Science Fiction"],
            "rating": 8.1
        },
        {
            "id": "18",
            "title": "Star Wars: Episode IV - A New Hope",
            "posterUrl": "https://image.tmdb.org/t/p/w500/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg",
            "synopsis": "Luke Skywalker joins forces to battle the Empire.",
            "genres": ["Action", "Adventure", "Science Fiction"],
            "rating": 8.6
        },
        {
            "id": "19",
            "title": "Back to the Future",
            "posterUrl": "https://image.tmdb.org/t/p/w500/fNOH9f1aA7XRTzl1sAOx9iF553Q.jpg",
            "synopsis": "Marty McFly, a 17-year-old high school student, is accidentally sent 30 years into the past.",
            "genres": ["Adventure", "Comedy", "Science Fiction"],
            "rating": 8.5
        },
        {
            "id": "20",
            "title": "Gladiator",
            "posterUrl": "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg",
            "synopsis": "A former Roman General sets out to exact vengeance against the corrupt emperor.",
            "genres": ["Action", "Drama", "Adventure"],
            "rating": 8.5
        },
        {
            "id": "21",
            "title": "Braveheart",
            "posterUrl": "https://image.tmdb.org/t/p/w500/or1gBugydmjToAEq7OZY0owwFk.jpg",
            "synopsis": "Scottish warrior William Wallace leads his countrymen in a rebellion.",
            "genres": ["Action", "Drama", "History"],
            "rating": 8.4
        },
        {
            "id": "22",
            "title": "The Lion King",
            "posterUrl": "https://image.tmdb.org/t/p/w500/2bXbqYdUdNVa8VIWXVfclP2ICtT.jpg",
            "synopsis": "A young lion prince flees his kingdom only to learn the true meaning of responsibility.",
            "genres": ["Animation", "Adventure", "Drama"],
            "rating": 8.5
        }
    ]
