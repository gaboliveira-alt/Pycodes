

def my_repr(self):
    return f'{type(self).__name__} ({self.__dict__})'

class Meta(type):
    def __new__(msc, name, bases, dct):
        print('Metaclass New')
        cls = super().__new__(msc, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = my_repr
        
        if 'speak' not in cls.__dict__ or not callable(cls.__dict__['speak']):
            raise NotImplementedError('Implemente este metodo para speak')
        
        return cls
    
    def __call__(cls, *args, **kwargs):
        instance_ = super().__call__(*args, **kwargs)
        
        if 'name' not in instance_.__dict__:
            raise NotImplementedError('Crie o atributo de name')
        
        return instance_


class Person(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instance_ = super.__new__(cls)
        return instance_
    
    def __init__(self, name):
        print('MEU INIT')
        # self.name = name
    
    def speak(self):
        print('FALARRRRRRRRRRRR')

p1 = Person('Luiz')
p1.speak()