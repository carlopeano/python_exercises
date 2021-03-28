favorite_numbers = {
    'andrea': [23, 14, 67],
    'marco': [41, 27],
    'gianmarco': [57, 45, 22],
    'annamaria': [78, 33],
    'loredana': [22, 69, 89, 91],
    }

for friend, numbers in favorite_numbers.items():
    print(f"{friend.title()}'favorite numbers are:")
    for number in numbers:
        print(number)