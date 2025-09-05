
print(globals())

def outside(x):
    a = x
    
    def inside():
        print(locals())
        return a
    return inside


inside01 = outside(10)
inside02 = outside(20)
print(inside01())
print(inside02())


def concatenation(initial_string):
    final_value = initial_string
    def internal(conca_value=''):
        nonlocal final_value
        final_value += conca_value
        return final_value
    return internal

c = concatenation('a')
print(c('b'))
print(c('c'))
print(c('d'))
print(c(''))