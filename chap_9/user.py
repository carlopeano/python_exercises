"""A class used to represent users"""


class User():
    """Attempt of a user profile"""

    def __init__(self, first_name, last_name, gender, phone_number, email):
        """Initiate attributes to describe a user profile"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone_number = phone_number
        self.email = email


    def describe_user(self):
        """Print description of the user"""
        if self.gender.lower() == 'male':
            print(f"\n{self.first_name.title()} {self.last_name.title()}'s " 
                f"phone number is {self.phone_number}.")
            print(f"His email address is {self.email}.")

        elif self.gender.lower() == 'female':
            print(f"\n{self.first_name.title()} {self.last_name.title()}'s "
                f"phone number is {self.phone_number}.")
            print(f"Her email address is {self.email}.")
            
        else:
            print("\nYou did not specify the gender. Please, choose " 
                "between 'female' and 'male' ")


    def greet_user(self):
        """print greetings to user"""
        print(f"\nHello {self.first_name.title()} {self.last_name}!")