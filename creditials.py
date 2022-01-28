from user import User

class Creditials:
    '''
    Creditials class will perform function to do with authentication with the aid of data from the user class
    '''
    def __init__(self):
        '''
        constructor function used for testing purposes during development
        '''
        pass
    
    @classmethod
    def login(cls, username: str, password):
        '''
        Login function will be used to authenticate the user. 
        use the saved credials and allow the user to login the appliaction
        '''
        for user in User.disply_user_accounts():
            if user.username == username and user.password == password:
                success = f"{username} have successfully logged in the application"
                return success
            else :
                error = f"No such username:({username}) found in the application. Please create an account or check your password!"
                return error    
        # print(User.disply_user_accounts())
