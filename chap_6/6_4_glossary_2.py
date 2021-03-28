glossary = {
    'print' : 'prints the variables and strings mentioned',
    'for' : 'is used for looping',
    'append' : 'adds a variable in a list',
    'del' : 'deletes variables, keys, etc',
    'range' : 'makes easy to generate a series of numbers',
    }
for key, value in glossary.items():
    print(f"{key}:\n{value}")

glossary['set'] = 'a method to eliminate the printing of duplicates from a list'
glossary['values'] = 'a method that allows to return a list of values without any keys'
glossary['keys'] = 'a method that allows to return a list of keys without any values'
glossary['items'] = 'a method that allows to return a list of keys and their values'
glossary['title'] = 'a method that allows to return a variable with the first letter in capital'

for key, value in glossary.items():
    print(f"\n{key}:\n{value}.")