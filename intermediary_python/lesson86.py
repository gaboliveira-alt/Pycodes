
product = {
    'name': 'CANETA AZUL',
    'price': 2.5,
    'category': 'Escritorio'
}


example_dict = {
    key: value.lower()
    if isinstance(value, str) else value
    for key, value in product.items()
    if key == 'category'
}

print(example_dict)


example_list = [
    ('a', 'value a'),
    ('b', 'value b'),
    ('c', 'value c'),
]

example_dict01 = {
    key: value 
    for key, value in example_list
}

print(dict(example_list))


example_set = {i ** 2 for i in range(10)}
print(set(range(20)))