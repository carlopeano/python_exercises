def describe_city(city_name, city_country='italy'):
    """ Display information about a city"""
    print(f"\n{city_name.title()} is in {city_country.title()}.")

describe_city('florence')
describe_city('berlin', 'germany')
describe_city(city_name='bari', city_country='italy')