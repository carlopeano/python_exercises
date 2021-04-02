responses = {}

poll_active = True

while poll_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, "
        "where would you go? ")
    responses[name] = response

    question = input("\nIs there another person after you? (yes/ no) ")

    if question.lower() == 'no':
        poll_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to go to "
        f"{response.title()} for a vacation.")

print()