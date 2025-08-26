
def falsy_or_truthy(value):
    return 'falsy' if not value else 'truthy'


example_list = [0]
example_dict = {}
example_set = set()
example_tuple = ()
string = ' '
example_int = 0
example_float = 0.0
example_none = None
false = False
example_range = range(0)


print(f'TESTE', falsy_or_truthy('TESTE'))
print(f'{example_list=}', falsy_or_truthy(example_list))
print(f'{example_dict=}', falsy_or_truthy(example_dict))
print(f'{example_set=}', falsy_or_truthy(example_set))
print(f'{example_tuple=}', falsy_or_truthy(example_tuple))
print(f'{string=}', falsy_or_truthy(string))
print(f'{example_int=}', falsy_or_truthy(example_int))
print(f'{example_float=}', falsy_or_truthy(example_float))
print(f'{example_none=}', falsy_or_truthy(example_none))
print(f'{false=}', falsy_or_truthy(false))
print(f'{example_range=}', falsy_or_truthy(example_range))