class User():
    """Attempt of a user profile"""

    def __init__(self, first_name, last_name, phone_number, email):
        """Initiate attributes to describe a user profile"""
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.login_attempts = 0


    def describe_user(self):
        """Print description of the user"""
        print(f"{self.first_name} {self.last_name}'s phone number is "
            f"{self.phone_number}. \nThe email address is {self.email}.")


    def greet_user(self):
        """print greetings to user"""
        print(f"Hello {self.first_name} {self.last_name}!")


    def increments_login_attempts(self):
        """Increments the number of login attempts by one"""
        self.login_attempts += 1


    def reset_login_attempts(self):
        """Reset the number of login attempts to zero"""
        self.login_attempts = 0




user_1 = User('Maria', 
            'Anzanova',
            '+489-693-69383036', 
            'maria.anzova@hmail.com')

print(f"Login attempts: {user_1.login_attempts}")

user_1.increments_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")

user_1.increments_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")

user_1.increments_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")

user_1.increments_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")

user_1.increments_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")

user_1.reset_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")