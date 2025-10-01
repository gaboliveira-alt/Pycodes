
def sum_numbers(x, y, /, a, b):
    print(x + y + a + b)
    

sum_numbers(1, 2, 3, b=1)


def sum_numbers01(x, y, *, c):
    print(x + y  + c)


sum_numbers01(1, y=2, c=3)


def sum_numbers02(x, y, /, *, c, **kwargs):
    print(kwargs)
    print(x + y + c)


sum_numbers02(1, 2, c=3, name='bora', receba=12)