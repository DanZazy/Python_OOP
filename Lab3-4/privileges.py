from enum import Enum

class Privileges(Enum):

    Add_User = 1
    Add_Message = 2
    Ban_User = 3
    Delete_User = 4

    @classmethod
    def show_privileges(cls):
        print("Admin privileges: ")
        for p in cls:
            print(p.value, p.name)