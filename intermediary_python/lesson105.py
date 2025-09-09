def factory_decorator(a=None, b=None, c=None):
    def factory_function(func):
        print('Decorador 1')
        def nested(*args, **kwargs):
            print('Parametros do decorador', a, b, c)
            print('Aninhada')
            result = func(*args, **kwargs)
            return result
        return nested
    return factory_function


@factory_decorator(1, 2, 3)
def sum_numbers01(x, y):
    return x + y


def decorator(func):
    print('Decorador 1')
    def nested(*args, **kwargs):
        print('Aninhada')
        result = func(*args, **kwargs)
        return result
    return nested


def blabla(a, b, c):
    print(a, b, c)
    return decorator


@blabla(1, 2, 3)
def sum_numbers(x, y):
    return x + y


multiplication = decorator(lambda x, y: x + y)

example_decorator = factory_decorator()
ten_plus_five = sum_numbers01(10, 5)
print(multiplication)
print(ten_plus_five)