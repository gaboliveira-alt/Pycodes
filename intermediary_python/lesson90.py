iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()
print(next(iterator))
print(next(iterator))
print(next(iterator))

example_list = [n for n in range(10000)]
example_generator = (n for n in range(10000))

for number in example_generator:
    print(number)

print(next(example_generator))
print(next(example_generator))
print(next(example_generator))