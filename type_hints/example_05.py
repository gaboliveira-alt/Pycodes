from example_03 import Animal
from example_04 import get_animal_name
from utils import cyan_print, sep_print


class Dog(Animal):
    def make_sound(self) -> None:
        cyan_print(f"{self.name=!r} faz auauauau")

    def run(self) -> None:
        cyan_print(f"{self.name=!r} está correndo muito...")

class Cat(Animal):
    def make_sound(self) -> None:
        cyan_print(f"{self.name=!r} faz miau miau")

class Car:
    def __init__(self, name: str):
        self.name = name


if __name__ == "__main__":
    dog = Dog("Mike")
    cat = Cat("Leitinho")
    car = Car("Ford")

    sep_print()

    get_animal_name(dog)
    get_animal_name(cat)
    # get_animal_name(car)

    dog.make_sound()
    cat.make_sound()
    # car.make_sound()

    sep_print()

    dog2: Animal
    dog2 = Dog("Dog 2")
    dog2.run()
