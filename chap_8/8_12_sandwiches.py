def making_sandwiches(*ingredients):
    """Print a summary of the sandwich that's being ordered"""
    print("\nThe sandwich has the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

# making_sandwiches('speck', 'brie')
making_sandwiches('cheese')
# making_sandwiches('mayo', 'ham', 'tomato')