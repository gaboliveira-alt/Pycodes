
class Animal:
    # name = 'Lion'
    
    def __init__(self, name):
        self.name = name
        
        variable = 'bora bill'
        print(variable)
    
    
    def eating(self, food):
        return f'{self.name} está comendo {food}'
    
    
    def execute(self, *args, **kwargs):
        return self.eating(*args, **kwargs)


lion = Animal('Mufasa')
print(lion.name)
print(lion.execute('Elefante'))
