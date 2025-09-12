
def params_decorator(name):
    print('Decorador', name)
    def decorator(func):
        def new_function(*args, **kwargs):
            result = func(*args, **kwargs)
            final = f'{result} {name}'
            return final
        return new_function
    return decorator


@params_decorator(name='5')
@params_decorator(name='4')
@params_decorator(name='3')
@params_decorator(name='2')
@params_decorator(name='1')
def sum_numbers(x, y):
    return x + y


ten_plus_five = sum_numbers(10, 5)
print(ten_plus_five)