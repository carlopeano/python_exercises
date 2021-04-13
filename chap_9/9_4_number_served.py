class Restaurant() :
    """A simple attempt to model a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type of the restaurant"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"{self.name}'s cuisine is {self.type}.")

    def open_restaurant(self):
        """Indicate the restaurant is open"""
        print(f"{self.name} is open!")


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


my_restaurant = Restaurant('Da Mario', 'Italian cuisine')
print(f"Restaurant's name: {my_restaurant.name}")
print(f"Cuisine's type: {my_restaurant.type}")


my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.read_number_served()

my_restaurant.number_served = 58
my_restaurant.read_number_served()


my_restaurant.set_number_served(68)
my_restaurant.read_number_served()

my_restaurant.increment_number_served(100)
my_restaurant.read_number_served()