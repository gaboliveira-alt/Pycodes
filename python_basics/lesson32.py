input_user = input("Digite um número: ")

try:
    int_input_user = int(input_user)
    
    if int_input_user % 2 == 0:
        print("Esse número é par!")
    else:
        print("Esse número é impar!")        
except:
    print("Isso não é um número!")




input_hour = input("Digite algum horario: ")

try:
    int_input_hour = int(input_hour)


    is_morning = int_input_hour >= 0 and int_input_hour <= 11
    is_afternoon = int_input_hour >= 12 and int_input_hour <= 17
    is_evening = int_input_hour >= 18 and int_input_hour <= 23


    if is_morning:
        print("Bom dia!")
    elif is_afternoon:
        print("Boa tarde!")
    elif is_evening:
        print("Boa noite!")
    else:
        print("Essa hora não existe!")
except:
    print("Digite apenas números!")



user_name_input = input("Digite seu nome: ")

lenght_name = len(user_name_input)
short_name = lenght_name <= 4
normal_name = lenght_name == 5 or lenght_name == 6
long_name = lenght_name > 6


if short_name:
    print("Seu nome é curto!")
elif normal_name:
    print("Seu nome é normal!")
elif long_name:
    print("Seu nome é longo!")