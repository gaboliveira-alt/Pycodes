
example_list = []
for x in range(3):
    for y in range(3):
        example_list.append((x, y))
print(example_list)


example_list01 = [(x, y) for x in range(3) for y in range(3)]
print(example_list01)

example_list02 = [[(x, char) for char in 'Francisco'] for x in range(3)]
print(example_list02)