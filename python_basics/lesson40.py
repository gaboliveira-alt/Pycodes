
while True:
    
    number_1 = input('Digite um número: ')
    number_2 = input('Digite outro número: ')
    operator = input('Digite algum dos operadores(+,-,*, ou /): ')
    valid_numbers = None
    float_number1 = 0
    float_number2 = 0
    
    
    try:
        float_number1 = float(number_1)
        float_number2 = float(number_2)
        valid_numbers = True
    except:
        valid_numbers = None
    
    
    if valid_numbers is None:
        print('Um ou ambos os números são invalidos. Digite apenas números')
        continue
    
    
    valid_operators = '+-*/'
    
    
    if operator not in valid_operators:
        print('Operador inválido')
        continue
    
    
    if len(operator) > 1:
        print('Só pode um operador.')
        continue
    
    
    if operator == '+':
        print(f'{float_number1}+{float_number2}=', float_number1 + float_number2)
    elif operator == '-':
        print(f'{float_number1}-{float_number2}=', float_number1 + float_number2)
    elif operator == '*':
        print(f'{float_number1}x{float_number2}=', float_number1 * float_number2)
    elif operator == '/':
        print(f'{float_number1}/{float_number2}=', float_number1 / float_number2)
    else:
        print('Não deveria chegar aqui.')
    
    
    exit_calculator = input("Quer sair? [s]sim: ").lower().startswith('s')
    
    
    if exit_calculator is True:
        break