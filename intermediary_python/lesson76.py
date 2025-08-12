import copy

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




person_02 = {}


key = 'name'

person_02[key] = 'Gabriel Oliveira'
person_02['surname'] = 'Pinto'


print(person_02[key])
print(person_02['surname'])


person_02[key] = 'Ruan'

del person_02['surname']
print(person_02)
print(person_02[key])

print(person_02.get('surname', 'Não existe'))




person_03 = {
    'name': 'Gabriel',
    'surname': 'Oliveira Pinto',
    'age': 900,
}


person_03.setdefault('age', 0)
print(person_03['age'])
print(person_03.__len__())
print(len(person_03))
print(person_03.keys())
print(person_03.values())
print(person_03.items())


for value in person_03.values():
    print(value)


for key, item in person_03.items():
    print(key, value)



d1 = {
    'k1': 1,
    'k2': 2,
    'k3': [0, 1, 2, 3],
}

d2 = d1.copy()


d2['k1'] = 1000
d2['k3'][0] = 999

print(d1)
print(d2)



d3 = {
    'k1': 1,
    'k2': 2,
    'k3': [0, 1, 2, 3],
}

d4 = copy.deepcopy(d3)

d4['k1'] = 200
d4['k3'][2] = 700


print(d3)
print(d4)




p1 = {
    'name': 'Gabriel',
    'surname': 'Oliveira Pinto',
}


print(p1['name'])
print(p1.get('name'), 'Não Existe')

name = p1.pop('name')
print(name)
print(p1)
last_key = p1.popitem()
print(last_key)
print(p1)
p1.update({
    'name': 'new value',
    'age': 30,
})
p1.update(name='new value', age=19)
example_tuple = (('name', 'new value'), ('age', 19))
example_list = [['name', 'new value'], ['age', 19]]
p1.update(example_tuple)
p1.update(example_list)