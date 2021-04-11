class Restaurants():
    """Attempt to represent a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    
    def describe_restaurant(self):
        """Print info of the restaurant"""
        print(f"{self.restaurant_name.title()} serves "
            f"{self.cuisine_type.title()} cuisine. ")


    def open_restaurant(self):
        """Print that the restaurant is open"""
        print(f"{self.restaurant_name.title()} is open now!")


restaurant_1 = Restaurants('Antonio', 'Italian')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurants('Naruto', 'Japanese')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurants('Lambada', 'Brazilian')
restaurant_3.describe_restaurant()
