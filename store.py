from products import Product

class Store:

    def __init__(self, product_list: list):
        """it initialises an instance of a store"""
        self.product_list = product_list


    def add_product(self, product):
        """it adds a product to the store"""
        self.product_list.append(product)


    def remove_product(self, product):
        """it removes a product from the store"""
        self.product_list.remove(product)


    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.quantity
        return total_quantity


    def get_all_products(self) -> list[Product]:
        """Returns all products in the store that are active."""
        active_products_list = []
        list_number = 0
        for product in self.product_list:
            if product.is_active():
                list_number += 1
                print(f"{list_number}. {product.show()}")
                active_products_list.append(product)
        return active_products_list


    def order(self, shopping_list) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        total_order_price = 0.0
        for product, quantity in shopping_list:
            total_order_price += product.buy(quantity)
        return total_order_price
