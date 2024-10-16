class Product():
    def __init__(self, name:str, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f'{self.name}, {self.price} EUR, {self.quantity} units'

class Electronics(Product):
    pass

class Clothing(Product):
    pass
        
class ShoppingCart():
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        
    def remove_product(self, product):
        self.products.remove(product)
        
    def calculate_total_cost(self):
        all_products = [product for product in self.products]
        total_cost = 0
        for pr in all_products:
            total_cost += (pr.price * pr.quantity) 
        return f'{total_cost:.2f}'
    
    def show_cart(self):
        return [str(product) for product in self.products]
        
    

product1 = Product('Glass', 2.34, 3)
product2 = Product('Chair', 20, 2)
clothes1 = Clothing('Nike', 19, 1)
electroncs1 = Electronics('LG', 200, 1)

shopping_cart = ShoppingCart()
shopping_cart.add_product(product1)
shopping_cart.add_product(product2)
shopping_cart.remove_product(product1)
shopping_cart.add_product(clothes1)
shopping_cart.add_product(electroncs1)


print(shopping_cart.calculate_total_cost())
print(shopping_cart.show_cart())