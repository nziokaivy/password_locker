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
    
    def delete_credential(self):
        """
        Method which deletes a particular credential
        """
        Credential.credentials_list.remove(self)

    @classmethod
    def find_by_name(cls, account_name):
        """
        Method that takes in a name and returns a credential that matches that particular name
        Args:
            name: account_name that has a password
        Returns:
            The account_name and it's corresponding PassWord
        """

        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential    

    @classmethod
    def credential_exists(cls, name):
        """Method to check whether a credential exists
        Args:
        name: name of account to search whether it exists
        boolean: True or False depending if the contatc exists
        """

        for credential in cls.credentials_list:
            if credential.account_name == name:
                return True
        return False

                

    
