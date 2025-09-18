import os

path_file = 'C:\\Users\\kylor\\OneDrive\\Documentos\\GitHub\\Pycodes\\example_pathfile\\'
path_file += 'lesson116.txt'


# example_file = open(path_file, 'w')

# example_file.close()


# with open(path_file, 'w+') as example_file:
#     example_file.write('Line 1\n')
#     example_file.write('Line 2\n')
#     example_file.writelines(
#         ('Line 4\n', 'Line 5\n')
#     )
#     example_file.seek(0, 0)
#     print(example_file.read())
#     print('Lendo')
#     print(example_file.readline(), end='')
#     print(example_file.readline().strip())
#     print(example_file.readline().strip())
#     print('READLINES')
#     example_file.seek(0, 0)
#     for line in example_file.readlines():
#         print(line.strip())

# print('#' * 10)

# with open(path_file, 'r'):
#     print(example_file.read())

with open(path_file, 'w', encoding='utf-8') as example_file:
    example_file.write('Atenção bora bill\n')
    example_file.write('Mais atenção ainda\n')
    example_file.writelines(
        ('Line 4\n', 'Line 5\n')
    )
    example_file.seek(0, 0)

# os.remove(path_file)
# os.rename(path_file, 'lesson116.txt')