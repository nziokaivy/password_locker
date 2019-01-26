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

    credentials_list = []    

    def save_credentials(self):
        """
        Method to save credential objects into credentials_list
        """
        self.credentials_list.append(self)
    
        

                

    
