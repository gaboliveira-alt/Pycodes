
#print(123)
#raise ValueError('Deu erro aqui')
#print(456)

def example_divide(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        return n


def example_divide01(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        print('----')
        raise


def not_accept_zero(d):
    if d == 0:
        raise ZeroDivisionError('Esse valor que voce enviou é 0')


def must_be_int_or_float(number):
    type_number = type(number)
    if not isinstance(number, (int, float)):
        raise TypeError(
            f'{number} deve ser um numero do tipo inteiro ou float'
            f'{type_number.__name__} enviado.'
        )


def division(n, d):
    must_be_int_or_float(n)
    must_be_int_or_float(d)
    not_accept_zero(d)
    return n / d


print(division(8, 2))