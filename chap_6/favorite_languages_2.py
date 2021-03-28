favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'ewdard': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

print()

# refined with if statement included to make the wording reflect the
# number of languages considered

for name, languages in favorite_languages.items():
    if len (languages) > 1:
        print(f"{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    elif len (languages) == 1:
        print(f" {name.title()}'s favorite language is:"
            f"\n\t{languages[0].title()}")
