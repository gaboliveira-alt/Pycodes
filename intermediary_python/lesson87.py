
example_list = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {1, 2}, {'nome': 'Gabriel'}]

for item in example_list:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))
    elif isinstance(item, str):
        print('STR')
        print(item.upper(), isinstance(item, str))
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
    else:
        print('OUTRO')
        print(item)