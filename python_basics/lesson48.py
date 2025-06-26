string = 'ABCDE'

example_list = [123, True, 'Luiz Otavio', 1.2, []]
print(example_list)
example_list[-3] = 'Francisco'
print(example_list)
print(example_list[2], type(example_list[2]))

example_list_01 = [10, 20, 30, 40]
example_list_01[2] = 300
del example_list[2]
print(example_list_01)
print(example_list_01[2])
example_list_01.append(50)
example_list_01.pop()
example_list_01.append(60)
example_list_01.append(70)
last_value = example_list_01.pop(3)
print(example_list, 'Removido', last_value)

example_list_02 = [10, 20, 30, 40]
example_list_02.append('Luiz')
name = example_list_02.pop()
example_list_02.append(1233)
del example_list_02[-1]
example_list_02.clear()
example_list_02.insert(100, 5)
print(example_list_02[4])

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
list_a.extend(list_b)
print(list_a)