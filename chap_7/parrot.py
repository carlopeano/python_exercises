# message = input("\nTell me something, and I will repeat it back to you: ")
# print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# message = ""

# while message != 'quit':
#     message = input(prompt)
    
#     if message != 'quit':
#         print(message)

# Let's add a flag that we call 'active'

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        print ("\nGame over\n")
    else:
        print(message)