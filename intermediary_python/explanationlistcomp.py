def divisionFn(x, y):
    return x / y


def multiplicationFn(x, y):
    return x * y


def exponetialFn(x, y):
    return x ** y


numbers = [1, 2, 3, 4, 5]
new_numbers = [number for number in numbers]

print(new_numbers)

division = [divisionFn(number, 2) for number in numbers]
multiplication = [multiplicationFn(number, 2) for number in numbers]
exponetial = [exponetialFn(number, 2) for number in numbers]

print(division)
print(multiplication)
print(exponetial)


new_numbers01 = [number for number in numbers if number > 5]
odds = [number for number in numbers if number % 2 != 0]
even = [number for number in numbers if number % 2 == 0]
other_if = [
    number
    if number >= 6 else 600
    for number in even
]

print(new_numbers01)
print(odds)
print(even)
print(other_if)


for x in range(1, 11):
    for y in range(1, 6):
        print((x, y))



lines_collums = [
    (x, y)
    if y != 2 else (x, y * 1000)
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 2
]

print(lines_collums)



string = 'Gabriel Oliveira'
new_string = ''.join(char for char in string)
print(new_string)

chars_number = 2
new_string01 = [string[char_index:char_index + chars_number] for char_index in range(0, len(string), chars_number)]
print(new_string01)

chars_number01 = 5
new_string02 = [string[char_index:char_index + chars_number01] for char_index in range(0, len(string), chars_number01)]

new_string03 = '.'.join([string[char_index:char_index + chars_number] for char_index in range(0, len(string), chars_number)])
print(new_string03)


names = ['Gabriel', 'Mariana', 'Fabricio', 'Francisco']
new_names = [f'{name[:-1].lower()}{name[-1].upper()}'for name in names]
print(new_names)


numbers_01 = [[number, number ** 2] for number in range(10)]
flat = [y for x in numbers_01 for y in x]
print(numbers_01)
print(flat)