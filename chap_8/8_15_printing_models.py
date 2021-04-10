# import printing_functions as pf


# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # You need to obviuosly call the 2 functions!
# pf.print_models(unprinted_designs, completed_models)
# pf.show_completed_models(completed_models)

from printing_functions import print_models as pm
from printing_functions import show_completed_models as scm


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs, completed_models)
scm(completed_models)