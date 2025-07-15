string = 'ABC'
names_list = ['Maria', 'Helena', 1, 2, 3, 'Mariana']
phrases_tuple = ('Python', 'é', 'legal')
classroom = [
    ['Maria', 'Helena'], ['Joao', 'Fabricio'], ['Gabriel', 'Mariana', (0, 2, 3, 4, 5)]
]

a, b, *_ = names_list
p, b, *_, u = names_list
p, b, *_, ap, u = names_list

for name in names_list:
    print(name, end=' ', sep=' ')

print(*names_list)
print(*phrases_tuple)
print(*string)
print(*classroom, sep='\n')