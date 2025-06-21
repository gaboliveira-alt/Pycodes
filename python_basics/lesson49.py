example_list = [10, 20, 30, 40]
example_list[2] = 300
del example_list[2]
print(example_list)
print(example_list[2])
example_list.append(50)
example_list.pop()
example_list.append(60)
example_list.append(70)
last_value = example_list.pop(3)
print(example_list, 'Removido', last_value)
