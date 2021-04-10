# Arbitrary number of Arguments

# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested"""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green pepper', 'extra cheese')


# def make_pizza(*toppings):
#     """Summarise the pizza we are about to make"""
#     print("\nMaking a pizza with the folllowing toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green pepper', 'extra cheese')


#M Mixing positional and arbitraty arguments

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size} inches pizza with the folllowing toppings:")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green pepper', 'extra cheese')