from user import User
from creditials import Creditials

new_user1 = User.user


def user_instance():
    '''
    user_instance function will create an instance of user.
    when a user creates an account this function saves the 
    user information into the list
    '''
    first_name = input("Enter your First name\n")
    last_name = input("Enter your Last name\n")
    username = input("Enter your username\n")
    password = input("Enter your Your password\n")

    new_user = User(first_name, last_name, username, password)
    new_user.save_user()
    new_user1.append(new_user)

def main():
    print("\n")
    print("Welcome to Password Lock Applictation. \n")
    User.generate_menu()

    choice = int(input("Enter a value:\n"))

    while True:
        # User.generate_menu()
        if choice == 1:
            print("***CREATE AN ACCOUNT***")
            user_instance()
            print("ACCOUNT CREATED")
            User.generate_menu_after_login()
            choice_creation = int(input("Enter a value:\n"))
            while True:
                if choice_creation == 1:
                    User.delete_user_account()
                    # new_user1.remove(new)
                    print("ACCOUNT SUCCESSFULY DELETED")
                    User.generate_menu()
                    choice = int(input("Enter a value:\n"))
                    break
                elif choice_creation == 2:
                    # print("Details of the available users!!")
                    Creditials.generate_all_saved_accounts()
                    # User.generate_menu_after_login()
                    User.generate_menu()
                    choice = int(input("Enter a value:\n"))
                    break
                elif choice_creation == 3:
                    User.generate_menu()
                    choice = int(input("Enter a value:\n"))
                    break
