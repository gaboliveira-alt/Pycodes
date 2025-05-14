
user_name = input("Digite seu nome: ")
user_age = input("Digite sua idade: ")

int_user_age = int(user_age)

if user_name and int_user_age:
    print(10 * '-')
    print(f'Seu nome é {user_name}')
    print(user_name[::-1])
    
    if user_age in ' ':
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')
        
    print(user_name[0])
    print(user_name[len(user_name) - 1])
    print(10 * '-')
else:
    print('Desculpe, você deixou campos vazios')