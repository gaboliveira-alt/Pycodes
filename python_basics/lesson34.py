condition = True

while condition:
    name = input('Qual seu nome? ')
    print(f'Seu nome é {name}')
    
    if name == 'sair':
        break

print('Acabou')