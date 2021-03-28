pets = {
    'fido': {
        'kind': 'dog',
        'gender': 'male',
        'age': 5,
        'owner': 'martin smith',
        },
    'red': {
        'kind': 'cat',
        'gender': 'female',
        'age': 3,
        'owner': 'laura rossi',
        },
    'grace': {
        'kind': 'turtle',
        'gender': 'female',
        'age': 12,
        'owner': 'mark preston'
        },
    }

print("We cure several pets here in our facilities:")

for name_pet, data_pet in pets.items():
    gender_pet = data_pet['gender']
    kind_pet = data_pet['kind']
    owner_pet = data_pet['owner']

    if gender_pet == 'male':
        print(f"\t{name_pet.title()} is a {gender_pet} {kind_pet} and his "
            f"owner is {owner_pet.title()}")

    elif gender_pet == 'female':
        print(f"\t{name_pet.title()} is a {gender_pet} {kind_pet} and her "
            f"owner is {owner_pet.title()}")