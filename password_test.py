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

    def tearDown(self):
            '''
            Method that cleans up after each test case has run.
            '''
            Account_user.users_list = []
    

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

    def test_save_multiple_user(self):
            '''
            Method to check if we can save multiple accounts
            objects to our users_list
            '''
            self.new_account.save_user()
            test_user = Account_user("Test","code500")
            test_user.save_user()
            self.assertEqual(len(Account_user.users_list),2)

    def test_find_user(self):
        '''
        Method to test whether the details in function find_user work
        '''

        self.new_account = Account_user("Ivy","Muffins01")
        self.new_account.save_user()
        test_user1 = Account_user("Test","pass1")
        test_user1.save_user()

        for user in Account_user.users_list:
			if user.first_name == test_user1.first_name and user.password == test_user1.password :
			   current_user = user.first_name
		       return found_user

        self.assertEqual(found_user,Credential.find_user(test_user1.first_name,test_user1.password))


if __name__ ==  '__main__':
    unittest.main()


