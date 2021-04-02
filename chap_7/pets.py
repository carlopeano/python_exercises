# Using remove() to remove a specific value from the list
pets = ['dog', 'cat','dog', 'goldfish','cat', 'rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)