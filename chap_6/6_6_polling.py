favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

friends = ['luca', 'silvia', 'jen', 'andrea', 'phil', 'mark', 'carlo', 'greg']

for name in friends:
    if name in favorite_languages:
        print(f"Dear {name.title()}, thank you for having taken the poll!")
    elif name not in favorite_languages:
        print(f"Dear {name.title()}, please take the poll!")