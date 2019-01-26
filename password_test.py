import unitttest
from password import Account_user

class TestAccount_user(unittest.TestCase):
    '''
    Test class that defines test cases for the account user behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating tets cases
    '''    

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
    self.new_account = Account_user("Ivy","Muffins001")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.first_name,"Ivy")
        self.assertEqual(self.new_account.password,"Muffins001")

        if __name__ == '__main__':
            unittest.main()

