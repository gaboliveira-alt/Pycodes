name = 'Gabriel'

print(name[2])
print(name[-4])
print('a' in name)
print('Gab' in name)
print(10 * '-')
print('Lelouch' in name)
print('el' not in name)
print('zero' not in name)


digit_name = input("Digite um nome: ")
finded = input("Digite o que voce quer encontrar: ")


if finded in digit_name:
    print(f'O caractere \"{finded}\" foi achado em {digit_name}')
else:
    print('Nada foi achado')