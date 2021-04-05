def make_shirt(message, size='large'):
    """"display the information on the T-shirt (default size large)"""
    print(f"\nThe size of the T-shirt is {size.title()}.")
    print(f"The message on the T-shirt is: '{message}'.")

make_shirt('Good things need time', 'medium')
make_shirt('Superman')
make_shirt(message='California', size='small')