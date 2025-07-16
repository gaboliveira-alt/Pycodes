import random
import re
import sys


for _ in range(50):
    user_request_cpf = ''
    for _ in range(9):
        user_request_cpf += str(random.randint(0, 9))
    count = 10
    mult_numbers = 0
    for number in user_request_cpf:
        mult_numbers += int(number) * count
        count -= 1

    first_digit = (mult_numbers * 10) % 11
    first_digit = first_digit if first_digit <= 9 else 0


    count_01 = 11
    mult_numbers_01 = 0
    for number in user_request_cpf:
        mult_numbers_01 += int(number) * count_01
        count_01 -= 1

    second_digit = (mult_numbers_01 * 10) % 11
    second_digit = second_digit if second_digit <= 9 else 0


    calculate_cpf = f'{user_request_cpf[:9]}{first_digit}{second_digit}'
    print(calculate_cpf)