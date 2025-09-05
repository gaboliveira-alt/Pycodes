
def sum_numbers(x, y):
    return x + y

def multiplication(x, y):
    return x * y

def create_function(function):
    def execute_function(*args):
        return function(*args)
    return execute_function

number_for_sum = create_function(sum_numbers)
number_for_multiplication = create_function(multiplication)

print(number_for_sum(5, 2))
print(number_for_multiplication(5, 5))


def better_create(function, x):
    def internal_function(y):
        return function(x, y)
    return internal_function


sum_for_five = better_create(sum_numbers, 5)
mult_for_ten = better_create(multiplication, 10)
print(sum_for_five(10))
print(mult_for_ten(8))