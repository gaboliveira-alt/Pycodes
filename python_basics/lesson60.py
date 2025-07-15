condition = 10 == 10
variable = 'Valor' if condition else 'Outro Valor'
print(variable)
digit = 10
new_digit = digit if digit <= 9 else 0
new_digit = 0 if digit > 9 else digit
print(new_digit)
print('Valor' if False else 'Outro Valor' if False else 'Fim')