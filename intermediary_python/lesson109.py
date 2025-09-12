from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


persons = [
    'João', 'Joana', 'Luiz', 'Leticia'
]

t_shirts = [
    ['preta', 'branca'],
    ['p', 'm'],
    ['masculino', 'feminino', 'unisex']
]


print_iter(combinations(persons, 2))
print_iter(permutations(persons, 2))
print_iter(product(t_shirts, repeat=2))