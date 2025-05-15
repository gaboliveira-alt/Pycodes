variable_1 = 'a'
variable_2 = 'b'

print(id(variable_1))
print(id(variable_2))


condition = False
pass_if = None

if condition:
    pass_if = True
    print("Faça algo")
else:
    print("Nâo faça algo")
    

if pass_if is None:
    print("Não passou no if")
else:
    print("Passou no if")
    
