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