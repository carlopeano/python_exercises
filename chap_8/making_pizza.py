# Using the module pizza.py in the directory for calling the function
# make_pizza and the different ways we can do it

# import pizza


# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green pepper', 'extra cheese')

# from pizza import make_pizza


# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green pepper', 'extra cheese')

# from pizza import make_pizza as mp


# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green pepper', 'extra cheese')

import pizza as p


p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green pepper', 'extra cheese')