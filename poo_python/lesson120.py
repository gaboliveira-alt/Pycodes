# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

string = 'Victoria'
print(string.upper())
print(isinstance(string, str))


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        


p1 = Person('Gabriel', 'Oliveira')
# p1.name = 'Gabriel'
# p1.surname = 'Oliveira'
print(p1.name)
print(p1.surname)


p2 = Person('Victoria', 'Uchoa')
# p2.name = 'Victoria'
# p2.surname = 'Uchoa'
print(p2.name)
print(p2.surname)