# requested_topping ='mushrooms'

# if requested_topping != 'anchovies':
#     print ("Hold the anchovies!")

# from page 86

# requested_toppings = ['mushrooms', 'green pepper', 'extra cheese']

# for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}.")
# print ("Finished making pizza!")

requested_toppings = ['mushrooms', 'green pepper', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green pepper':
        print (f"Sorry, we are out of {requested_topping} right now.")
    else:
        print(f"Adding {requested_topping}.")

print ("\nFinished making pizza!")