
class A:
    def __new__(cls, *args, **kwargs):
        print('Eu sou o new')
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, x):
        self.x = x
        print('Eu sou o init aqui')

a = A(123)
print(a.x)