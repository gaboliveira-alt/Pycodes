user_input = input("(E)ntrar ou (S)air? ")
password_digit = input("Digite uma senha numerica: ")

int_password_digit = int(password_digit)
password_perm = 123456


if user_input == 'E' and int_password_digit == password_perm:
    print("Voce entrou")
else:
    print("Saiu")



print(True and False and True)
print(True and 0 and True)
