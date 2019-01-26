# import pyperclip
import random
class Account_user:
    """
    Class to create new user accounts and save information
    """

    users_list = []

    def __init__(self,first_name,password):
    
        '''
        Method that helps us define properties that each user account will have
    
        Args:
          first_name : account user name
          password : account password
        '''

        self.first_name = first_name
        self.password = password

    def save_user(self):

        '''
        Method to save new user account objects into users_list
        '''

        Account_user.users_list.append(self)     



class Credential:
    """
    Class that create account credentials ,save the information and generate passwords.
    """
    credentials_list = []
    user_credentials_list = []

    @classmethod
    def find_user(cls,first_name,password):
        '''
        Method that checks if the name and password entered matches the saved accounts in the users_list 

        Args:
            first_name: user name to search for
            password : user password to search for

        Returns :
            user that matches the first name and password.
        '''
        current_user = ''
        for user in cls.users_list:
            if (user.first_name == firsts_name and user.password == password):
                current
                return current_user = user.first_name


    
