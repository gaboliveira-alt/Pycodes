from functools import partial
from types import GeneratorType


def print_iter(iterator):
    print(*list(iterator), sep='\n')


def increase_percentage(value, percentage):
    return round(value * percentage, 2)


increase_ten_percent = partial(
    increase_percentage,
    percentage=1.1
)


def change_product_price(product):
    return {**product, 'price': increase_ten_percent(product['price'])}


products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


new_products = [
    {**product, 'price': increase_ten_percent(product['price'])} for product in products
]


new_products01 = list(map(change_product_price, products))


print_iter(products)
print_iter(new_products)
print_iter(new_products01)


print(list(map(lambda x: x * 3, [1, 2, 3, 4])))