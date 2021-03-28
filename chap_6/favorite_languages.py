favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }
language = favorite_languages['sarah'].title()
print(f"Sarah favorite language is {language}\n")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()} ")

print()

for name in favorite_languages.keys():
    print(name.title())

print()

for name in favorite_languages:
    print(name.title())

print()

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}!")

    if name in friends:
        language = favorite_languages[name].title()
        print(f'Dear {name.title()}, I see that you like {language}!')
    
if 'erin' not in favorite_languages.keys():
    print(f"\nErin, please take our pool!")

print()

# looping through a dictionary in a particular order

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the pool!")

print()

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print()

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())