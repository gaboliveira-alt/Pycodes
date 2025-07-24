
def saudation(msg, name):
    return f'{msg}, {name}'


def execute_function(function, *args):
    return function(*args)


print(execute_function(saudation, 'Bom dia', 'Gabriel'))
print(execute_function(saudation, 'Boa noite', 'Maria'))