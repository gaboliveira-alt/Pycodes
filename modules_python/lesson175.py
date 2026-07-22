import json
import os

FILE_NAME = "lesson175.json"

path_make_json_file = os.path.abspath(
    os.path.join(os.path.dirname(__file__), FILE_NAME)
)

movie_cinema = {
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",

    "is_movie": True,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": None
}

with open(path_make_json_file, "w") as file_json:
    json.dump(movie_cinema, file_json, ensure_ascii=False, indent=2)

with open(path_make_json_file) as file_json:
    movie_json = json.load(file_json)
    print(movie_json)
