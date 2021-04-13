from user import User
from admin import Admin
from admin import Priviledges


a_user = Admin('mark',
            'zuckemberg',
            'male',
            '+34-356-662294',
            'mz@lmail.com')

a_user.greet_user()
a_user.describe_user()

a_user.priviledges.show_priviledges()

# user_a = Admin('Charles', 
#                 'Bronson', 
#                 'male',
#                 '+39-349-6938560', 
#                 'c_bronson@mail.it')

# user_a.describe_user()
# user_a.priviledges.show_priviledges()

# user_b = Admin('sarah',
#                 'connor',
#                 'female',
#                 '+44-678-12345098',
#                 'sarah.connor@fmail.de')

# user_b.describe_user()
# user_b.priviledges.show_priviledges()