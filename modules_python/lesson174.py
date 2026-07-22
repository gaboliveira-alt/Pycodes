import json
from typing import TypedDict


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


string_json: str = """
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
"""

movie_cinema: Movie = json.loads(string_json)
print(movie_cinema)
print(movie_cinema["title"])
print(movie_cinema["characters"][0])

json_movie = json.dumps(movie_cinema, ensure_ascii=False, indent=2)
print(json_movie)
