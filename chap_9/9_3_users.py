class User():
    """Attempt of a user profile"""

    def __init__(self, first_name, last_name, phone_number, email):
        """Initiate attributes to describe a user profile"""
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email


    def describe_user(self):
        """Print description of the user"""
        print(f"{self.first_name} {self.last_name}'s phone number is "
            f"{self.phone_number}. \nThe email address is {self.email}.")


    def greet_user(self):
        """print greetings to user"""
        print(f"Hello {self.first_name} {self.last_name}!")


user_1 = User('Maria', 
            'Anzanova',
            '+489-693-69383036', 
            'maria.anzova@hmail.com')

user_1.describe_user()
user_1.greet_user()

user_2 = User('Andrea',
            'Koristos',
            '+43-54-5343632',
            'ak@koristos.he')

user_2.describe_user()
user_2.greet_user()

user_3 = User('Loredana', 
            'Branget',
            '+33-02-6939485',
            'lo_branget@gmail.fr')

user_3.describe_user()
user_3.greet_user()