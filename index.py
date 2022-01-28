from user import User
from creditials import Creditials

new_user1 = User.user


def user_instance():
    '''
    user_instance function will create an instance of user. when a user creates an account this function saves the user information into the list
    '''
    first_name = input("Enter your First name\n")
    last_name = input("Enter your Last name\n")
    username = input("Enter your username\n")
    password = input("Enter your Your password\n")

    new_user = User(first_name, last_name, username, password)
    new_user.save_user()
    new_user1.append(new_user)
