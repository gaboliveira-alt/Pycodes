
a, b = 1, 2
a, b = b, a
print(a, b)

person = {
    'name': 'Gabriel',
    'surname': 'Oliveira',
}

a, b = person
print(a, b)

person_01 = {
    'name': 'Gabriel',
    'surname': 'Oliveira',
}

a_01, b_01 = person_01.values()
print(a_01, b_01)

person_02 = {
    'name': 'Gabriel',
    'surname': 'Oliveira',
}

a_02, b_02 = person_02.items()
print(a_02, b_02)

person_03 = {
    'name': 'Gabriel',
    'surname': 'Oliveira',
}

(a1, a2), (b1, b2) = person_03.items()
print(a1, a2)
print(b1, b2)

for value in person_03.items():
    print(value)

for key, value in person_03.items():
    print(key, value)
    

person_04 = {
    'name': 'Gabriel',
    'surname': 'Pinto',
}

data_person = {
    'age': 19,
    'width': 1.78,
}

complete_person = {**person_04, **data_person}
print(complete_person)


def show_kwargs(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)
    
    for key, value in kwargs.items():
        print(key, value)

show_kwargs(1, 2, 3,name='Gabriel', surname='Oliveira Pinto')
show_kwargs(**complete_person)


configurations = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

show_kwargs(**configurations)