
def gen01():
    print('COMECOU O GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU O GEN1')

    
def gen02(gen=None):
    print('COMECOU O GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU O GEN02')


def gen03():
    print('COMECOU O GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU O GEN 3')



g1 = gen02(gen01())
g2 = gen02(gen03())
g3 = gen02()

for n in g1:
    print(n)
print()
for n in g2:
    print(n)
print()
for n in g3:
    print(n)
print()