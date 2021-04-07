def city_country(city, country):
    """Return info about cities"""
    full_info = f"{city}, {country}"
    return full_info.title()

city_info = city_country('brussels', 'belgium')
print(city_info)

city_info = city_country('rome', 'italy')
print(city_info)

city_info= city_country('berlin', 'germany')
print(city_info)