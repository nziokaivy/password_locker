import unitttest
from password import Account_user

class TestAccount_user(unittest.TestCase):
    '''
    Test class that defines test cases for the account user behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating tets cases
    '''    

    defsetUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_account = Account_user("Ivy","Muffins001")
    