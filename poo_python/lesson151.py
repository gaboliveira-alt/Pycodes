
def my_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

    
def add_repr(cls):
    cls.__repr__ = my_repr
    return cls

@add_repr
class Time:
    def __init__(self, name):
        self.name = name

@add_repr
class Planet:
    def __init__(self, name):
        self.name = name


example_time = Time('Brasil')
example_time1 = Time('Dinamarca')

example_planet = Planet('Terra')
example_planet1 = Planet('Marte')

print(example_time)
print(example_time1)

print(example_planet)
print(example_planet1)