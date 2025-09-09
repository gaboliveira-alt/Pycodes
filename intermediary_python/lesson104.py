def create_function(func):
    def internal(*args, **kwargs):
        print('Ok vou te decorar.')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        result += ' Bora bill'
        print(f'O seu valor é {result}')
        print('Ok você foi decorado')
        return result
    return internal


@create_function
def string_invert(string):
    print(f'{string_invert.__name__}')
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('o seu parametro não é uma string, altere para o tipo compativel.')


inverted_string = string_invert('Gabriel')
print(inverted_string)