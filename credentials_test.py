import unittest
from credentials import Credential

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating tets cases
    ''' 
       
    def setUp(self):
        '''
        Method to run before each test cases.
        '''
        self.new_account = Account_user("Ivy","Muffins01")

    