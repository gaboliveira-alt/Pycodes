
user_request_cpf = input('Informe o seu CPF: ')
numbers_cpf_raw = list(user_request_cpf)
numbers_cpf_str = []


for number in numbers_cpf_raw:
    if number == '.' or number == '-':
        continue
    numbers_cpf_str.append(number)


new_numbers_cpf_str = []
new_numbers_cpf_str.extend(numbers_cpf_str[0:9])


number_cpf_formated = []
for number in new_numbers_cpf_str:
    number_cpf_formated.append(int(number))


count = 10
mult_numbers = 0
for number in number_cpf_formated:
    mult_numbers += number * count
    count -= 1

first_digit = (mult_numbers * 10) % 11
first_digit = first_digit if first_digit <= 9 else 0
print(first_digit)




numbers_cpf_raw_01 = list(user_request_cpf)
numbers_cpf_str_01 = []


for number in numbers_cpf_raw_01:
    if number == '.' or number == '-':
        continue
    numbers_cpf_str_01.append(number)


new_numbers_cpf_str_01 = []
new_numbers_cpf_str_01.extend(numbers_cpf_str_01[0:10])


number_cpf_formated_01 = []
for number in new_numbers_cpf_str_01:
    number_cpf_formated_01.append(int(number))


count_01 = 11
mult_numbers_01 = 0
for number in number_cpf_formated_01:
    mult_numbers_01 += number * count_01
    count_01 -= 1

second_digit = (mult_numbers_01 * 10) % 11
second_digit = second_digit if second_digit <= 9 else 0
print(second_digit)