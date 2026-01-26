
class Person:
    cpf = '09090'
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def speak_class_name(self):
        print('Classe Pessoa aqui')
        print(self.name, self.surname, self.__class__.__name__)


class Client(Person):
    def speak_class_name(self):
        print('Classe Cliente aqui')
        print(self.name, self.surname, self.__class__.__name__)


class Student(Person):
    cpf = 'cpf do aluno aqui'


client_01 = Client('Gabriel', 'Oliveira')
client_01.speak_class_name()
print(client_01.cpf)

student_01 = Student('Roberta', 'Jamily')
student_01.speak_class_name()
print(student_01.cpf)