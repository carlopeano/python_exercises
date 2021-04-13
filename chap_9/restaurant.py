"""A class used to represent restaurants."""

class Restaurant() :
    """A simple attempt to model a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type of the restaurant"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"\n{self.name.title()}'s cuisine is {self.type.title()}.")

    def open_restaurant(self):
        """Indicate the restaurant is open"""
        print(f"{self.name.title()} is open!")


    def read_number_served(self):
        """Print a statement with the number of customers served"""
        print(f"\nThe customers served in {self.name.title()} is "
            f"{self.number_served}.")


    def set_number_served(self, number_customers):
        """Set the number of customers that have been served"""
        if number_customers >= self.number_served:
            self.number_served = number_customers
        else:
            print("You can't decrease the number of customers that "
                "have been served")


    def increment_number_served(self, customers):
        """Increase the number of customers that have been served"""
        if customers >= 0:
            self.number_served += customers
        else:
             print("You can't decrease the number of customers that "
                "have been served")


