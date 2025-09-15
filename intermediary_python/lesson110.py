from itertools import groupby

students = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def order_by_note(student):
    return student['nota']


students_01 = ['a', 'a', 'a', 'a', 'b', 'c', 'a']
groups = groupby(sorted(students_01))

for key, group in groups:
    print(key)
    print(list(group))
print()


grouped_students = sorted(students, key=order_by_note)
grouped_list = groupby(grouped_students, key=order_by_note)

for key, group in grouped_list:
    print(key)
    for student in group:
        print(student)