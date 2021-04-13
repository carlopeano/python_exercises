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
        if self.gender == 'male' or 'Male':
            print(f"\n{self.first_name.title()} {self.last_name.title()}'s " 
                f"phone number is {self.phone_number}.")
            print(f"His email address is {self.email}.")

        elif self.gender == 'female'or 'Female' :
            print(f"\n{self.first_name.title()} {self.last_name.title()}'s "
                f"phone number is {self.phone_number}.")
            print(f"Her email address is {self.email}.")
            
        else:
            print("\nYou did not specify the gender. Please, choose " 
                "between 'female' and 'male' ")


    def greet_user(self):
        """print greetings to user"""
        print(f"\nHello {self.first_name} {self.last_name}!")


class Admin(User):
    """represent the admin, that is a particular kind of user"""

    def __init__(self, first_name, last_name, gender, phone_number, email):
        """Initialize attributes of the parent class"""
        super().__init__(first_name, last_name, gender, phone_number, email)
        self.priviledges = ["can add post", 
                            "can delete post",
                            "can ban users",
                            "can feel the Golden God"]


    def show_priviledges(self):
        """prints the list of priviledges of an admin"""
        print(f"\n{self.first_name.title()} {self.last_name.title()} "
            f"has the following priviledges:")
        n = 1

        for self.priviledge in self.priviledges:
            print(f"{n}. {self.priviledge.title()}")
            n += 1


user_a = Admin('Charles', 
                'Bronson', 
                'male',
                '+39-349-6938560', 
                'c_bronson@mail.it')

user_a.describe_user()
user_a.show_priviledges()

user_b = Admin('sarah',
                'connor',
                'female',
                '+44-678-12345098',
                'sarah.connor@fmail.de')

user_b.describe_user()
user_b.show_priviledges()