import decimal

number_01 = decimal.Decimal('0.1')
number_02 = decimal.Decimal('0.7')
result = number_01 + number_02
print(result)
print(f'{result:.2f}')
print(round(result, 2))