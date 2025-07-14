
for char in 'ABC':
    print(char)


example_list = ['Gabriel', 'Alan', 'Fabricio']

for name in example_list:
    print(name)


example_list2 = ['Maria', 'Helena', 'Luiz']
example_list2.append('Gabriel')


list_index = range(len(example_list2))

for names_index in list_index:
    print(names_index, example_list2[names_index], type(example_list2[names_index]))