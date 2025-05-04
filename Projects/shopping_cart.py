def create_shopping_cart():
    shopping_cart = []
    shopping_cart.append("apple")
    shopping_cart.append("banana")
    shopping_cart.append("milk")

    print("Shopping Cart Contents:")
    for item in shopping_cart:
        print(f"{item}")

    return shopping_cart

# Call the function
my_cart = create_shopping_cart()