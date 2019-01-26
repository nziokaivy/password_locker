class Credential:
    """
    Class that create account credentials ,save the information and generate passwords.
    """
    def __init__(self, account_name, account_password):
        '''
        Method that helps us define properties that each user account credentials will have
    
        Args:
          account_name : account user name
          account_password : account password
        '''

        self.account_name = account_name
        self.account_password = account_password

    def save_credentials(self):
        """
        Method to save credential objects into credentials_list
        """
        self.credentials_list.append(self)    




    credentials_list = []
   

    @classmethod
    def find_user(cls,first_name,password):
        '''
        Method that checks if the name and password entered matches the saved accounts in the users_list 

        Args:
            first_name: user name to search for
          

        Returns :
            user that matches the first name.
        '''
        found_user = ''
        for user in cls.credentials_list:
            if (user.first_name == firsts_name and user.password == password):
                found_user = user.first_name
                return found_user

                

    
