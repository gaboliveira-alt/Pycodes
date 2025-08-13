
def execute(function, *args):
    return function(*args)



def sum_numbers(x, y):
    return x + y


def create_mult(multiplicator):
    def mult_number(number):
        return number * multiplicator
    return mult_number



duplicate = execute(lambda m: lambda n: n * m, 2)
print(duplicate(2))


print(execute(lambda x, y: x + y, 3, 3))


print(execute(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7))