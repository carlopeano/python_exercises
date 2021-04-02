sandwich_orders = ['caprese', 'speck and brie', 'jam and cheese', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich} sandwich.")

print("\nThe last sandwiches we finished are:")
for sandwich in finished_sandwiches:
    print(sandwich)