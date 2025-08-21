import pprint

def better_print(example_list):
    pprint.pprint(example_list, sort_dicts=False, width=40)


example_list = []
for number in range(10):
    example_list.append(number)
print(example_list)


example_list01 = [number for number in range(10)]
print(example_list01)

example_list02 = [number * 3 for number in range(20)]
print(example_list02)



example_list03 = []
for number in range(10):
    example_list03.append(number)


example_list04 = [
    number * 2 for number in range(10)
]

print(list(range(10)))
print(example_list04)


products = [
    {'name': 'p1', 'price': 20},
    {'name': 'p2', 'price': 10},
    {'name': 'p3', 'price': 30},
]

new_products = [product for product in products]
print(*new_products, sep='\n')

new_products01 = [product['name'] for product in products]
print(*new_products01, sep='\n')

new_products02 = [{'name': product['name'], 'price': product['price']} for product in products]
print(*new_products02, sep='\n')

new_products03 = [
    {**product, 'price': product['price'] * 1.05} 
    if product['price'] > 20 else {**product}
    for product in products
    ]


better_print(products)
example_list05 = [n for n in range(10) if n < 5]

new_products04 = [
    {**product, 'price': product['price'] * 1.05}
    if product['price'] > 20 else {**product}
    for product in products
    if (product['price'] >= 20 and product['price'] * 1.05) > 10
]