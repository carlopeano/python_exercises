responses = {}

# Set a flag to indicate that the polling is active
polling_active = True

while polling_active:
    # Prompt the person name and response.
    name = input("\nWhat's your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Polling is compleate. Show the results
print(f"\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")

print()