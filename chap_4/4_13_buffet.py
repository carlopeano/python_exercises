original_foods = ('martini carrots', 'peperonata', 'avocado salad', 
	'salmon in oven', 'bruger')

print("This is the original buffet:")
for original_food in original_foods:
	print(original_food.title())

#It's a tuple so it's immmutable and I can check it as follow:
#original_foods[0] = 'salad'
#Yes, it's immutable

new_foods = ('martini carrots', 'peperonata', 'caesar salad', 'bruger', 
	'tiramisu')

print("\nThis is the new buffet")
for new_food in new_foods:
	print(new_food.title())