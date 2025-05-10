
user_name = input("Digite seu nome: ")
user_age = input("Digite sua idade: ")

if user_name and user_age:
    print(10 * '-')
    print(f'Seu nome é {user_name}')
    print(user_name[-1:-8:-1])
    print(user_name in ' ')
    print(user_name[0])
    print(user_name[len(user_name) - 1])
    print(10 * '-')
else:
    print('Desculpe, você deixou campos vazios')