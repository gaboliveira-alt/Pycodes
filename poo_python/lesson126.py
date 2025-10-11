
class Person:
    actual_year = 2022
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    def get_birth_year(self):
        return Person.actual_year - self.age


data_person = {'name': 'Victoria', 'age': 19}
p1 = Person(**data_person)
p1.name = 'EITA'
print(p1.name)
p1.__dict__['bora'] = 'bill'
p1.__dict__['name'] = 'EITA'
del p1.__dict__['name']
print(p1.__dict__)
print(vars(p1))
print(p1.outra)
print(p1.name)
print(vars(p1))
print(p1.name)