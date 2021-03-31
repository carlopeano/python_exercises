prompt = "\nHow old are you? "
prompt += "\n(Enter 'quit' when you have finished). "

active = True

while active:
    age = input(prompt)

    if age == 'quit':
        active = False

    else:
        age = int(age)

        if age < 3:
            print("\nThe ticket is free.")
        elif age <= 12:
            print("\nThe ticket is $10.")
        elif age > 12:
            print("\nThe ticket is $15.")