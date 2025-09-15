
def print_iter(iterator):
    print(*list(iterator), sep='\n')


def filter_price(product):
    return product['price'] > 100


products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


new_products = [
    product for product in products
    if product['price'] > 100
]


new_products01 = filter(lambda product: product['price'] > 100, products)


new_products02 = filter(filter_price, products)


print_iter(new_products)
print_iter(new_products01)
print_iter(new_products02)