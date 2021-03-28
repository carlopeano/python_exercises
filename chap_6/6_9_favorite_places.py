favorite_places = {
    'carlo': ['florence', 'venice', 'sardinia'],
    'veronica':['paris','cagliari', 'berlin'],
    'mark':['bali', 'new york', 'dublin'],
    }

for person, places in favorite_places.items():
    print(f"{person.title()} favorite places are:")
    for place in places:
        print(f"-\t{place.title()} ")