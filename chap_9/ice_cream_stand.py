
"""A class used to represent ice cream stand."""

from restaurant import Restaurant


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
        print("\nThe ice cream's flavours are:")
        for self.flavour in self.flavours:
            print(f"\t- {self.flavour.title()}")


    def describe_restaurant(self):
        """Ice cream is not a cuisine"""
        print(f"\n{self.name.title()} sells {self.type}.")