
class Car:
    def __init__(self, name):
        self.name = name
    
    def accelerate(self):
        print(f'{self.name} está acelerando...')



mustang = Car('Mustang')
print(mustang.name)
Car.accelerate(mustang)
mustang.accelerate()

bmw = Car('BMW')
print(bmw.name)
Car.accelerate(bmw)
bmw.accelerate()