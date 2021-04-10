def make_car(manufacturer, model, **car_info):
    """Store info about cars in a dictionary"""
    car_info['car_manufacturer'] = manufacturer
    car_info['car_model'] = model
    return car_info

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)

# car = make_car('fiat', 500, color='white', sunroof=True)
# print(f"\n{car}")