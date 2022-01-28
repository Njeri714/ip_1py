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
        self.assertEqual(self.new_user.last_name, "Waweru)
        self.assertEqual(self.new_user.username, "njeri")
        self.assertEqual(self.new_user.password, "714")
