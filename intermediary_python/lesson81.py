
example_list = [4, 32, 1, 34, 5, 6, 6, 21]

example_list.sort()
print(example_list)

example_list01 = [4, 32, 1, 34, 5, 6, 6, 21]
example_list01.sort(reverse=True)
print(example_list01)


def order_list(item):
    return item['name']

def order_list01(item):
    return item['surname']

example_list02 = [
    {'name': 'Luiz', 'surname': 'miranda'},
    {'name': 'Maria', 'surname': 'Oliveira'},
    {'name': 'Daniel', 'surname': 'Silva'},
    {'name': 'Eduardo', 'surname': 'Moreira'},
    {'name': 'Aline', 'surname': 'Souza'},
]

example_list02.sort(key=order_list)

for item in example_list02:
    print(item)
    

example_list03 = [
    {'name': 'Luiz', 'surname': 'miranda'},
    {'name': 'Maria', 'surname': 'Oliveira'},
    {'name': 'Daniel', 'surname': 'Silva'},
    {'name': 'Eduardo', 'surname': 'Moreira'},
    {'name': 'Aline', 'surname': 'Souza'},
]

example_list03.sort(key=order_list01)

for item in example_list03:
    print(item)


example_list04 = [
    {'name': 'Luiz', 'surname': 'miranda'},
    {'name': 'Maria', 'surname': 'Oliveira'},
    {'name': 'Daniel', 'surname': 'Silva'},
    {'name': 'Eduardo', 'surname': 'Moreira'},
    {'name': 'Aline', 'surname': 'Souza'},
]

example_list04.sort(key=lambda item: item['name'])

for item in example_list04:
    print(item)
    

    
def exibition(list_dict):
    for item in list_dict:
        print(item)


example_list04 = [
    {'name': 'Luiz', 'surname': 'miranda'},
    {'name': 'Maria', 'surname': 'Oliveira'},
    {'name': 'Daniel', 'surname': 'Silva'},
    {'name': 'Eduardo', 'surname': 'Moreira'},
    {'name': 'Aline', 'surname': 'Souza'},
]


l1 = sorted(example_list04, key=lambda item: item['surname'])
l2 = sorted(example_list04, key=lambda item: item['name'])

exibition(l1)
exibition(l2)