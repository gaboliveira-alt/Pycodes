
class Person:
    
    year = 2023
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def class_method_example(cls):
        print('Hey Biney')
    
    
    @classmethod
    def create_50_age(cls, name):
        return cls(name, 50)
    
    
    @classmethod
    def create_no_name(cls, age):
        return cls('Anonimo', age)


p1 = Person('Victoria', 19)
Person.class_method_example()
p2 = Person.create_50_age('Marcão')
p3 = Person('Anonima', 20)
p4 = Person.create_no_name(30)
print(p2.name, p2.age)
print(p3.name, p3.age)
print(p4.name, p4.age)