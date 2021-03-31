prompt = "\nPlease write toppings for your pizza:"
prompt += "\n(Enter 'quit' when you have finished) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"We have added {topping} to your pizza!")