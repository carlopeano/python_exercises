
from restaurant import Restaurant
from ice_cream_stand import IceCreamStand


my_restaurant = Restaurant('Da Mario', 'Italian cuisine')
print(f"Restaurant's name: {my_restaurant.name}")
print(f"Cuisine's type: {my_restaurant.type}")


my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.read_number_served()

my_restaurant.set_number_served(25)
my_restaurant.read_number_served()

my_restaurant.increment_number_served(100)
my_restaurant.read_number_served()

ice_cream_stand = IceCreamStand('bar corso', 'ice cream')

ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.display_flavours()

ice_cream_stand.read_number_served()

ice_cream_stand.increment_number_served(254)
ice_cream_stand.read_number_served()