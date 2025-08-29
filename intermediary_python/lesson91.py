
def generator(n=0):
    yield 1
    print('Continuando...')
    yield 2
    print('Mais uma vez...')
    yield 3
    print('Vou terminar!')
    return 'ACABOU!'


gen = generator()
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))


for n in gen:
    print(n)
    

def generator_range(min=0, maximum=10):
    while True:
        yield min
        min += 1
        
        
        if min >= maximum:
            return


gen01 = generator_range()
for n in gen01:
    print(n)