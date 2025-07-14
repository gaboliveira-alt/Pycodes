list_names = ['Maria', 'Helena', 'Luiz']
list_names.append('Gabriel')

enumerate_list = enumerate(list_names)
print(next(enumerate_list))

for item in enumerate_list:
    print(item)


print('O que tem na lista enumerada:', enumerate_list)


for item in enumerate_list:
    print(item)


list_names1 = ['Gabriel', 'Luiz', 'Portacio']
list_names1.append('João')

enumerate_list1 = list(enumerate(list_names1))
print(enumerate_list1)


for item in enumerate(list_names1):
    item_index, name = item
    print(item_index, name)


for item_index, name in enumerate(list_names1):
    print(item_index, name, list_names1[item_index])


for item in enumerate(list_names1):
    print('FOR DA TUPLA')
    for value in item:
        print(f'\t{value}')