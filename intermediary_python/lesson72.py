
def multi_numbers(*args):
    total = 1
    for number in args:
        print('Total: ', total, number)
        total *= number
    return total


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
result_sum = multi_numbers(*numbers)
print(result_sum)


def even_or_odd(number):
    if number % 2 == 0:
        return 'É par'
    elif number % 2 != 0:
        return 'É impar'


even_odd = even_or_odd(4)
print(even_odd)


def even_or_odd_better(number):
    is_multiple = number % 2 == 0
    
    if is_multiple:
        return f'{number} é par!'
    return f'{number} é ímpar!'


print(even_or_odd_better(2))
print(even_or_odd_better(4))
print(even_or_odd_better(5))
print(even_or_odd_better(8))
print(even_or_odd_better(12))
