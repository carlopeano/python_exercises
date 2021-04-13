class Restaurant() :
    """A simple attempt to model a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type of the restaurant"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"{self.name.title()}'s cuisine is {self.type.title()}.")

    def open_restaurant(self):
        """Indicate the restaurant is open"""
        print(f"{self.name.title()} is open!")


    def read_number_served(self):
        """Print a statement with the number of customers served"""
        print(f"The customers served in {self.name.title()} is "
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


class IceCreamStand (Restaurant):
    """A simple attempt to model a specific restaurant: an ice cream stand"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initiate attributes of the parents class"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavours = ['chocolate',
                        'cream',
                        'fior di latte',
                        'torrone',
                        'stracciatella',
                        'haselnut',
                        'pistacchio',
                        'lemon',
                        'strawberry',
                        'peach',
                        'blackberry',
                        'raspberry']


    def display_flavours(self):
        """Print the list of the flavours"""
        print("The ice cream's flavours are:")
        for self.flavour in self.flavours:
            print(f"- {self.flavour.title()}")


    def describe_restaurant(self):
        """Ice cream is not a cuisine"""
        print(f"{self.name.title()} sells {self.type}.")



my_restaurant = Restaurant('Da Mario', 'Italian cuisine')
print(f"Restaurant's name: {my_restaurant.name}")
print(f"Cuisine's type: {my_restaurant.type}")


my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print()

ice_cream_stand = IceCreamStand('bar corso', 'ice cream')

ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.display_flavours()