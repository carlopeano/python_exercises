sandwich_orders = ['pastrami', 'caprese', 'pastrami', 'speck and brie', 
    'pastrami', 'jam and cheese', 'pastrami', 'tuna']
finished_sandwiches = []

print("Unfortunately, the deli has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe last sandwich we finished are:")
n = 1
for sandwich in finished_sandwiches:  
    print(f"{n}. {sandwich} sandwich")
    n += 1