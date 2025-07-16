
request_cpf = input('Informe o seu CPF: ')
numbers_cpf_raw = list(request_cpf)
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