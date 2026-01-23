
class ShopCart:
    def __init__(self):
        self._products = []
    
    def total(self):
        return sum([product.price for product in self._products])
    
    def insert_products(self, *products):
        # self._products.extend(products)
        # self._products += products
        for product in products:
            self._products.append(product)
    
    def show_products(self):
        print()
        for product in self._products:
            print(product.name, product.price)
        print()


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


shopping_cart = ShopCart()
product_01 = Product('Camiseta', 20.50)
product_02 = Product('Caneta', 12.40)
product_03 = Product('Boné', 6.70)

shopping_cart.insert_products(product_01, product_02, product_03)
shopping_cart.show_products()

print(shopping_cart.total())