import sandwiches


sandwiches.making_sandwiches('speck', 'brie')


from sandwiches import making_sandwiches

making_sandwiches('cheese')


from sandwiches import making_sandwiches as ms

ms('mozzarella', 'ham', 'tomato')

import sandwiches as sd 

sd.making_sandwiches('ham', 'tomato')

from sandwiches import *

making_sandwiches('cheese','raw ham')