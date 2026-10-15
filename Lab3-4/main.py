from user import User
from admin import Admin
from privileges import Privileges

user1 = User("John", "Doe", 30, "Male")
user1.describe_user()

admin1 = Admin("Jack", "Doe", 45, "Male")
admin1.describe_user()
admin1.priv.show_privileges()