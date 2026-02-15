from threading import activeCount


class Product:
    def __init__(self, name, price, quantity):
        """
        Initiator (constructor) method.
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity), raises an exception.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        # error handling on the input still to implement

    def get_quantity(self):
        """
        Getter function for quantity.
        Returns the quantity (int).
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Setter function for quantity.
        If quantity reaches 0, deactivates the product.
        """
        self.quantity = quantity
        if self.quantity <= 0:
            self.active = False

    def is_active(self) -> bool:
        """
        Getter function for active.
        Returns True if the product is active, otherwise
        False.
        """
        return  self.active



    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self):
        """
        Prints a string that represents the product, for example:
        "MacBook Air M2, Price: 1450, Quantity: 100"
        """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """
        - Buys a given quantity of the product.
        - Returns the total price (float) of the purchase.
        - Updates the quantity of the product.
        - In case of a problem (when? think about it), raises an Exception.
        """
        new_quantity = self.quantity - quantity
        self.set_quantity(new_quantity)
        return float(quantity * self.price) # returns the price in dollars

        #error handling still to be handled
