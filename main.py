from products import Product


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.get_quantity())

print(f"${bose.buy(2)}")

print(bose.get_quantity())