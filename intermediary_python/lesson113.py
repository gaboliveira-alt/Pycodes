from functools import reduce

products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def reduce_function(accumulator, product):
    print('acumulador', accumulator)
    print('produto', product)
    print()
    return accumulator + product['preco']


total_reduce = reduce(reduce_function, products, 0)
lambda_reduce = reduce(lambda ac, p: ac + p['preco'], products, 0)


total = 0
for p in products:
    total += p['preco']

print(round(total, 2))

print(sum(product['preco'] for product in products))
