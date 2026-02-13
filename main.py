from products import Product
from store import Store

product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)

for product in best_buy.product_list:
    product.show()

"""
bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.get_quantity())

print(f"${bose.buy(2)}")

print(bose.get_quantity())
"""