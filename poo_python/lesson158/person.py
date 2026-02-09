
from abc import ABC


class Person(ABC):
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
    
    @property
    def person_name(self):
        return self._name
    
    @person_name.setter
    def person_name(self, name: str):
        self._name = name
    
    @property
    def person_age(self):
        return self._age
    
    @person_age.setter
    def person_age(self, age: int):
        self._age = age