def multiple_number(number1, number2):
    result = number1 % number2 == 0
    print(f'{number1} é multiplo de {number2}?', end=' ')
    print(result)


multiple_number(16, 8)
multiple_number(15, 3)
multiple_number(10, 2)