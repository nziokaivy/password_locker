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
          first_name :  main account user name
          password :  main account password
        '''

        self.first_name = first_name
        self.password = password

    def save_user(self):

        '''
        Method to save new user account objects into users_list
        '''

        Account_user.users_list.append(self)     



if __name__ == '__main__':
    main()