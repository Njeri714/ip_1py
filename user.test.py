import unittest # module for testing 
from user import User

class TestUser(unittest.TestCase):
    '''
    Testuser forn testing user cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_user = User("Crispus", "njenga", "engineer", "1234")

    def tearDown(self):
        '''
        tear down function for clearing the list after every test
        '''
        User.user = []
    def test_init(self):
        '''
        test_init test the instances of user class before each test runs
        '''    
        self.assertEqual(self.new_user.first_name, "Charity")
        self.assertEqual(self.new_user.last_name, "waweru")
        self.assertEqual(self.new_user.username, "njeri")
        self.assertEqual(self.new_user.password, "714")

def test_save_user(self):
        '''
        test_save_user case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user), 2)
    
def test_find_user_account(self):
        '''
        test_find_user_account to check if we can find a user by username
        '''
        self.new_user.save_user()
        another_user = User("Hamida", "mstafa", "tm", "134")
        another_user.save_user()

        find_user = User.find_user_account("tm")
        print(find_user, another_user.username)
        self.assertEqual(find_user, another_user.username)



if __name__ == '__main__':
    unittest.main()