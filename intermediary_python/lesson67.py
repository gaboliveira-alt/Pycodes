
def sum(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


sum(1, 2)
sum(3, 5)
sum(100, 200)
sum(7, 9, 0)
sum(y=9, z=0, x=2)