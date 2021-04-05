def make_shirt(size,message):
    """Display information about a T-shirt"""
    print(f"\nThe size of the T-shirt is {size.title()}.")
    print(f"The message on the T-shirt is: '{message.title()}'.")

make_shirt('s','superman')
make_shirt(size='m', message="good things need time")