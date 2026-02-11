from dataclasses import dataclass

@dataclass
class Person:
    name: str
    surname: str
    
    @property
    def complete_name(self):
        return f'{self.name} {self.surname}'
    
    @complete_name.setter
    def complete_name(self, str_value: str):
        name, *surname = str_value.split()
        self.name = name
        self.surname = ''.join(surname)
    

@dataclass(init=False)
class Person1:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
        self.complete_name = f'{self.name} {self.surname}'
        
    def __post_init__(self):
        print('POST INIT')
    