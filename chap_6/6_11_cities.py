cities = {
    'bologna': {
        'country': 'italy',
        'population': 388_367,
        'fact':'it has the oldest existing universities in continuous '
            'operation in the world',
        },
    'brussels': {
        'country': 'belgium',
        'population': 1_208_542,
        'fact': 'it was founded in 979',
        },
    'berlin': {
        'country':'germany',
        'population': 3_769_495,
        'fact':'it is the capital of germany',
        },
    }
for city, data in cities.items():
    print(f"Regarding the city of {city.title()}, we have the "
        f"following information")
    
    country_city = data['country']
    pop_city = data['population']
    fact_city = data['fact']

    print(f"\tCountry: {country_city.title()}")
    print(f"\tPopulation: {pop_city}")
    print(f"\tFact: {fact_city}")
