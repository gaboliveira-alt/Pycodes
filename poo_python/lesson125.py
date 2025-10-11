
class Person:
    actual_year = 2022
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    def get_birth_year(self):
        return Person.actual_year - self.age


p1 = Person('Victoria', 18)
p2 = Person('Gabriel', 19)

print(Person.actual_year)
# Person.actual_year = 1

print(p1.get_birth_year())
print(p2.get_birth_year())