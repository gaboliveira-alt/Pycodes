
class Car:
    def __init__(self, name):
        self.name = name
    
    def accelerate(self):
        print(f'{self.name} está acelerando...')



string = 'Victoria'
print(string.upper())


mustang = Car('Mustang')
print(mustang.name)
mustang.accelerate()

bmw = Car('BMW')
print(bmw.name)
bmw.accelerate()