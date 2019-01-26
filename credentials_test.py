import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating tets cases
    ''' 

    def setUp(self):
        '''
        Method to run before each test cases.
        '''
        self.new_credential = Credential("Instagram","1122")

    

    def tearDown(self):
            '''
            Method that cleans up after each test case has run.
            '''
            Credential.credentials_list = []


    def test_credentials(self):
        """
        Method that tests whether the new_credentials have been instantiated correctly
        """
        self.assertEqual(self.new_credential.account_name, "Instagram")
        self.assertEqual(self.new_credential.account_password, "1122")  
 
    def test_save_credentials(self):
        """
        Method that tests whether the new created credential has been saved
        """
        self.new_credential.save_credentials()
        self.assertEqual(len(Credential.credentials_list), 1)

    def test_save_multiple_credentials(self):
        """
        Method that saves multiple credentials to credentials_list
        """
        self.new_credential.save_credentials()
        new_test_credential = Credential("Uber", "1234")
        new_test_credential.save_credentials()
        self.assertEqual(len(Credential.credentials_list), 2)
    

    def test_find_credential_by_name(self):
        """
        Test to check if we can find credential by name and return credential.
        """
        self.new_credential.save_credentials()
        new_test_credential = Credentials("Instagram", "1122")
        new_test_credential.save_credentials()

        found_credential = Credential.find_by_name("Instagram")

        self.assertEqual(found_credential.account_name, new_test_credential.account_name)

    def test_display_all_credentials(self):
        """
        TestCase to test whether all contacts can be displayed
        """
        self.assertEqual(Credential.display_credentials(), Credential.credentials_list)   

if __name__ == '__main__':
    unittest.main()        

            

    