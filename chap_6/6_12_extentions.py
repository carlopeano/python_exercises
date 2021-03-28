users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'gender': 'male',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'gender': 'female',
        },
    'efermi':{
        'first': 'enrico',
        'last': 'fermi',
        'location': 'chicago',
        'gender': 'male',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

    gender_user = user_info['gender']
    if gender_user == 'male':
        print(f"{full_name.title()} lives in {location.title()} and "
            f"his username is {username}.")
    elif gender_user == 'female':
        print(f"{full_name.title()} lives in {location.title()} and "
            f"her username is {username}.")