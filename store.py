from typing import Optional
from products import Product

class Store:

    def __init__(self, product_list: list):
        """it initilises an istance of a store"""
        self.product_list = product_list

    def add_product(self, product):
        """it adds a product to the store"""
        self.product_list.append(product)

    def remove_product(self, product):
        """it removes a product from the store"""
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        pass

    def get_all_products(self) -> list[Product]:
        """Returns all products in the store that are active."""
        for product in self.product_list:
            if product.is_active():
                product.show()


    def order(self, shopping_list) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        pass