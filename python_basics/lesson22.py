user_input = input("(E)ntrar ou (S)air? ")
password_digit = input("Digite uma senha numerica: ")

int_password_digit = int(password_digit)
password_perm = 123456


if (user_input == 'E' or user_input == 'e') and int_password_digit == password_perm:
    print("Voce entrou")
else:
    print("Saiu")


password = input('Senha: ') or 'Sem senha'
print(password)

test = 0 or False or 0 or 'abc' or True