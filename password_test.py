import unittest
from password import Account_user

class TestAccount_user(unittest.TestCase):
    '''
    Test class that defines test cases for the account user behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating tets cases
    '''    

    def setUp(self):
        '''
        Method to run before each test cases.
        '''
        self.new_account = Account_user("Ivy","Muffins01")
    

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.first_name,"Ivy")
        self.assertEqual(self.new_account.password,"Muffins01")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_account.save_user() 
        self.assertEqual(len(Account_user.users_list),1)

    


if __name__ ==  '__main__':
    unittest.main()


