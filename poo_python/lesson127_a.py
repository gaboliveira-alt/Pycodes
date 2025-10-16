import json

PATH_FILE = 'C:\\Users\kylor\\OneDrive\\Documentos\\GitHub\\Pycodes\\poo_python\\'
PATH_FILE += 'lesson127.json'


class Person:
    def __init__(self, name='Victoria', age=19):
        self.name = name
        self.age = age


p1 = Person('Gabriel', 19)
p2 = Person('Marcos Vinicius', 21)
p3 = Person('Murilo', 19)
list_persons = [vars(p1), vars(p2), vars(p3)]


def make_dump():
    with open(PATH_FILE, 'w', encoding='UTF-8') as class_file:
        print('FAZENDO DUMP')
        json.dump(list_persons, class_file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    print('ELE É O __main__')
    make_dump()
