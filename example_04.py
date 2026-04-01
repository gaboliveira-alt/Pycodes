from example_03 import Animal
from utils import cyan_print, sep_print


def get_animal_name(animal: Animal) -> None:
    cyan_print(f"'get_animal_name' | Classe: {type(animal).__name__}")
    cyan_print(f"'get_animal_name' | Classe: {type(animal).__name__}")
    sep_print()

if __name__ == "__main__":
    dog = Animal("Dog")
    cat = Animal("Cat")

    sep_print()

    get_animal_name(dog)
    get_animal_name(cat)
