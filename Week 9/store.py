import json

class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

class Store:
    def __init__(self):
        self.cart = []
        with open(r"E:/Python/CS50x/Week 9/project/data/products.json", "r") as file:
            products_data = json.load(file)
            self.products = []
            for item in products_data:
                product = Product(item["name"], item["category"], item["price"])
                self.products.append(product)



    def display_products(self):
        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product.name} - {product.category} - ${product.price}")

    def search_product(self, name):
        for item in self.products:
            if item.name.lower() == name.lower():
                return item
        return None


    def add_to_cart(self, product):
        self.cart.append(product)

    def get_total_price(self):
        total = sum(item.price for item in self.cart)
        return total
