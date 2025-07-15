classroom = [
    ['Maria', 'Helena'], ['Joao', 'Fabricio'], ['Gabriel', 'Mariana', (0, 2, 3, 4, 5)]
]

print(classroom)
print(classroom[0][0])
print(classroom[0][1])
print(classroom[1][0])
print(classroom[1][1])
print(classroom[2][2][3])

classroom_01 = [
    ['Maria', 'Helena'], ['Joao', 'Fabricio'], ['Gabriel', 'Mariana']
]

for classschool in classroom_01:
    print(f'a sala é {classschool}')
    for member in classschool:
        print(member)
