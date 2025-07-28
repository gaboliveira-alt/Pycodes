
person = dict(name='Gabriel', surname='Oliveira')
print(person, type(person))


person_01 = {
    'name': 'Gabriel',
    'surname': 'Oliveira Pinto',
    'age': 19,
    'height': 1.78,
    'addresses': [
        {'road': 'rua tal', 'number': 123},
        {'road': 'tal rua', 'number': 456},
    ],
}


print(person_01['name'])
print(person_01['surname'])
print()

for key in person_01:
    print(key, person_01[key])