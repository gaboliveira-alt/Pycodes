
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
from products_data import products
import copy


new_products = [
    {**product, 'price': f'{product['price'] * 1.10:.2f}'} for product in copy.deepcopy(products)
]

print(*products, sep='\n')
print()
print(*new_products, sep='\n')
print()


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)


products_sorted_name = [
    product for product in copy.deepcopy(sorted(products, key=lambda grown: grown['name']))
]

print(*products_sorted_name, sep='\n')
print()


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


products_sorted_price = [
    product for product in copy.deepcopy(sorted(products, key=lambda grown: grown['price']))
]

print(*products_sorted_price, sep='\n')
print()
print(*products, sep='\n')