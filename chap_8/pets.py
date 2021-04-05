# # Positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# # Keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='dog', pet_name='willie')

# Default values
def describe_pet (pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='red')
describe_pet('fido')
describe_pet(pet_name='harry', animal_type='hamster')