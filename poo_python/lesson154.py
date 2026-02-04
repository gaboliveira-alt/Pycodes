

class Multiplication:
    def __init__(self, multi) -> None:
        self.multi = multi
    
    def __call__(self, func) :
        def nested(*args, **kwargs):
            func_return = func(*args, **kwargs)
            return func_return * self.multi
        return nested


@Multiplication(10)
def func_sum(x, y):
    return x + y


four_plus_four = func_sum(4, 4)
print(four_plus_four)