number_str = input("Digite um número:")

try:
    print('STR:', number_str)
    number_float = float(number_str)
    print('FLOAT:', number_float)
    print(f'O dobro de {number_float} é {number_float * 2}')
except:
    print('Isto não é um número')
    

if number_str.isdigit():
    float_number = float(number_str)
    print(f'O dobro de {float_number} é {float_number * 2}')
else:
    print("Isso não é um número")