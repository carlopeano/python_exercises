prompt = "Dear Client, we currently have a limited number of tables available. "
prompt += "Could you please tell us how many people are you? "

seating = input (prompt)

seating = int(seating)

if seating > 8:
    print("\nWe are sorry, but you will have to wait for a table some minutes.")
else:
    print("\nYour table is ready.")