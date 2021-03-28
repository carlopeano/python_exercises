car = 'subaru'

print ("Is car == 'subaru'? I predict True.")
print (car == 'subaru')

print ("\nIs car == 'audi'? I predict False. ")
print (car == 'audi')

# Test 1 (True)
age = 41

print ("\nIs my age <= 45? I predict True.")
print(age <= 45)

#Test 2 (False)
age = 46

print ("\nIs my brother's age <= 45? I predict False.")
print(age <= 45)

#Test 3 (True)
favourite_pizza = 'bufalina'

print("\nIs my favourite_pizza != margherita? I predict True.")
print (favourite_pizza != 'margherita')

#Test 4
print ("\nIs my favourite_pizza != bufalina? I predict False.")
print (favourite_pizza!= 'bufalina')

#Test 5
pizzas = ['margherita', 'bufalina', 'napoletana', 'capricciosa']

print ("\nIs bufalina in the menu ? I predict True.")
print ('bufalina' in pizzas)

# Test 6
print("\nIs romana in the menu? I predict False.")
print('romana' in pizzas)

# Test 7
if 'siciliana' not in pizzas:
    print ("\nPizza siciliana is not in the menu")

# Test 8
if 'margherita' not in pizzas:
    print ("\nPizza margherita should be in the menu")
else:
    print("\nPizza margherita is obviously in the menu")

# Test 9
age_my = 32
age_you = 26

print((age_my >= 30) and (age_you <= 32))

# Test 10

print ((age_my ==30) and (age_you <= 32))

# Test 11
print ((age_my == 30) or (age_you <= 32))

