
class MyError(Exception):
    pass


class OtherError(Exception):
    ...


def raise_exception():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Olha o item 1')
    exception_.add_note('Você errou ali mano')
    raise exception_


try:
    raise_exception()
except MyError as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OtherError('Vou lançar outro erro novamente!')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma')
    raise exception_ from error