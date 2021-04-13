"""A set of classes used to represent admins and priviledges"""

from user import User


class Priviledges:
    """An simple attempt to model the priviledges of an admin"""

    def __init__(self, priviledge_list = ["can add post", 
                            "can delete post",
                            "can ban users",
                            "can feel like the Golden God"]):
        """Initialize attributes of priviledges"""
        self.priviledge_list = priviledge_list


    def show_priviledges(self):
        """prints the list of priviledges of an admin"""
        print(f"\nThe Admin has the following priviledges:")
        n = 1

        for self.priviledge in self.priviledge_list:
            print(f"{n}. {self.priviledge}")
            n += 1


class Admin(User):
    """represent the admin, that is a particular kind of user"""

    def __init__(self, first_name, last_name, gender, phone_number, email):
        """Initialize attributes of the parent class"""
        super().__init__(first_name, last_name, gender, phone_number, email)
        self.priviledges = Priviledges()