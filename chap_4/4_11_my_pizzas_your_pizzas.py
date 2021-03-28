pizzas = ['verace', 'bufalina', 'napoletana', 'margherita']
for pizza in pizzas:
	print(f"My favorite pizza is {pizza}.")
print(f"I know, they are all so tasty! I really	love pizza!")

friend_pizzas = pizzas[:]

pizzas.append('siciliana')
friend_pizzas.append('romana')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)