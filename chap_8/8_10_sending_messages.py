def send_messages(messages):
    """
    Print every message
    Move each message to a new list called sent_messages
    """
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

text_messages = [
    "Hey, how are you?",
    "I miss you my Dear",
    "Life is beautiful",
    "It's raining today",
    "I've bought the present for Mary",
    ]
sent_messages = []

send_messages(text_messages)