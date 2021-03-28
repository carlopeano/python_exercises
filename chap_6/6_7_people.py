people = {
    'mrossi': {
        'first_name': 'mario', 
        'last_name' : 'rossi', 
        'age' : 34, 
        'city' : 'Brussels',
        },
    'ssmith': {
        'first_name': 'sarah', 
        'last_name' : 'smith', 
        'age' : 28, 
        'city' : 'milan',
        },
    'lcasta': {
        'first_name': 'laetitia',
        'last_name': 'casta',
        'age': 41,
        'city': 'paris,'
        }
    }

for user_name, user_data in people.items():
    print(f"{user_name}:")
    full_name = f"{user_data['first_name']} {user_data['last_name']}"
    user_age = user_data['age']
    location = user_data['city']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tAge: {user_age}")
    print(f"\tCity: {location.title()} ")