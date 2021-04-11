class Restaurant() :
    """A simple attempt to model a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type of the restaurant"""
        self.name = restaurant_name
        self.type = cuisine_type


    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"{self.name}'s cuisine is {self.type}.")

    def open_restaurant(self):
        """Indicate the restaurant is open"""
        print(f"{self.name} is open!")





my_restaurant = Restaurant('Da Mario', 'Italian cuisine')
print(f"Restaurant's name: {my_restaurant.name}")
print(f"Cuisine's type: {my_restaurant.type}")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()