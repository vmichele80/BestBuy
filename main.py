
from products import Product
from store import Store

textual_menu =  """\
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
"""

def start(store):
    """Handle the textual menu and the input of the user"""
    print(textual_menu)
    user_choice = input("Please choose a number: ")
    if user_choice == "1":
        store.get_all_products()
        print("")
    elif user_choice == "2":
        print(f"Total of {store.get_total_quantity()} items in store")
        print("")
    elif user_choice == "3":
        shopping_list = []
        store.get_all_products()
        add_to_shopping_list(shopping_list)
        try:
            total = store.order(shopping_list)
            print("********")
            print(f"Order made! Total payment: ${total}\n")
        except Exception as e:
            print(f"Something went wrong with the order: \n{e} \n ")

    elif user_choice == "4":
        print("Thank you for visiting our store!")
        exit()
    else:
        print("You have entered a wrong option")


def add_to_shopping_list(shopping_list):
    """
    this function creates the shopping list
    I need to create a list of tuples with product name and quantity
    """
    print("When you want to finish order, enter empty text.")
    while True:
        try:
            product_choice = input("Which product # do you want?")
            if product_choice == "":
                return shopping_list

            product_choice = int(product_choice)

            if 0 < product_choice <= len(product_list):
                available_items = product_list[product_choice - 1].quantity
                quantity = int(input(f"What amount do you want? Max {available_items} available:\n"))
                if 0 < quantity <= available_items:
                    shopping_list.append((product_list[product_choice - 1], quantity))
                    print("Product added to shopping list!\n")
                else:
                    print(f"We could not place your order. We only have {available_items}")
            else:
                print("Please choose a product offered by our store\n")
        except ValueError:
            print("You need to enter an integers for the items or their quantity\n")

# setup initial stock of inventory
product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

# initialises the store
best_buy = Store(product_list)


def main():
    """Function welcome the user to the store and initialises the textual UI"""
    print("Welcome to our Best Buy store!\n")
    while True:
        start(best_buy)


if __name__ == "__main__":
    main()
