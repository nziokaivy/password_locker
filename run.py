#!/usr/bin/env python3.6

import random
import sys
from password import Account_user
from credentials import Credential

def create_userAccount(uname, password):
    '''
    Function that creates a new user
    '''
    new_userAccount = Account_user(uname, password)
    return new_userAccount

def save_userAccount(user):
    '''
    Function that saves a new user
    '''
    user.save_user()


def del_userAccount(user):
    '''
    Function that deletes a user 
    '''
    user.delete_user()

def create_new_credential(account_name, account_password):
    '''
    Function that creates a new account and its credentials
    '''
    new_credential = Credential(account_name, account_password)
    return new_credential

def save_new_credential(credentials):
    '''
    Function that saves the newly created account and password
    '''
    credentials.save_credentials()

def find_credential(account_name):
        '''
        Function that finds credentials using the account_name provided
        '''
        return Credential.find_by_name(account_name)

def check_existing_credentials(name):
        '''
        Function that checks whether a particular account and its credentials exist when searched using the account_name
        '''
        return Credential.find_by_name(name)  

def delete_credential(credentials):
        '''
        Function that deletes credentials
        '''
        return Credential.delete_credential(credentials)


def display_credentials():
        '''
        Function which displays all saved credentials
        '''
        return Credential.display_credentials() 

def generate_password():
    '''
    Function that generates a random password
    '''
    gen_pass = Credential.generate_password()
    return gen_pass  

def verify_user(name):
	'''
	Function that checks if the username already exists
	'''
	ver_user = Credential.find_by_name(name)
	return ver_user
     

def main(): 
    print('''                                                                                                                                                      
                                                                                     ##       ###                          /                            
                                                                                      ##       ###                       #/                             
                                                                                      ##        ##                       ##                             
                                     ##                                               ##        ##                       ##                             
                                     ##                                               ##        ##                       ##                             
   /###     /###      /###     /###   ##    ###    ####      /###   ###  /###     ### ##        ##      /###     /###    ##  /##      /##  ###  /###    
  / ###  / / ###  /  / #### / / #### / ##    ###     ###  / / ###  / ###/ #### / #########      ##     / ###  / / ###  / ## / ###    / ###  ###/ #### / 
 /   ###/ /   ###/  ##  ###/ ##  ###/  ##     ###     ###/ /   ###/   ##   ###/ ##   ####       ##    /   ###/ /   ###/  ##/   /    /   ###  ##   ###/  
##    ## ##    ##  ####     ####       ##      ##      ## ##    ##    ##        ##    ##        ##   ##    ## ##         ##   /    ##    ### ##         
##    ## ##    ##    ###      ###      ##      ##      ## ##    ##    ##        ##    ##        ##   ##    ## ##         ##  /     ########  ##         
##    ## ##    ##      ###      ###    ##      ##      ## ##    ##    ##        ##    ##        ##   ##    ## ##         ## ##     #######   ##         
##    ## ##    ##        ###      ###  ##      ##      ## ##    ##    ##        ##    ##        ##   ##    ## ##         ######    ##        ##         
##    ## ##    /#   /###  ## /###  ##  ##      /#      /  ##    ##    ##        ##    /#        ##   ##    ## ###     /  ##  ###   ####    / ##         
#######   ####/ ## / #### / / #### /    ######/ ######/    ######     ###        ####/          ### / ######   ######/   ##   ### / ######/  ###        
######     ###   ##   ###/     ###/      #####   #####      ####       ###        ###            ##/   ####     #####     ##   ##/   #####    ###       
##                                                                                                                                                      
##                                                                                                                                                      
##                                                                                                                                                      
 ##                                                                                                                                                     
                                                                                                                                                        
                                                                                                                                                                                                                               


     .--------.
    / .------. \
   / /        \ \
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  | LOCK |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'
                                                                                           

''')
    print("Hello Welcome to password locker!") 
    print("What is your name?")
    user_name = input()
    print(f"Hello {user_name}! What would you like to do?")
    print('\n')   

    while True:
        print("Use these short codes to select an option: Create New User use 'cn': Login to your account use 'lg' or 'ex' to exit password locker")
        short_code = input().lower()
        
        if short_code == 'cn':
                            print ("Enter username:")
                            create_user_name = input()
                            print("Create a password")
                            create_user_password = input()
                            print("Confirm Your Password")
                            confirm_password = input()
                            print(f" {create_user_name} your new user account has been created")
                            print ('\n')


                            while confirm_password != create_user_password:
                                print("Sorry your passwords did not match!")
                                print("Enter a password")
                                create_user_password = input()
                                print("Confirm Your Password")
                                confirm_password = input()

                            else:
                                print(f" Congratulations {create_user_name}! You have created a new account.")
                                print('\n')
                                print("Proceed to Log In to your Account")
                                print("Username")
                                entered_username = input()
                                print("Your Password")
                                entered_password = input()

                            while entered_username != create_user_name or entered_password != create_user_password:
                                print("You entered a wrong username or password")
                                print("Username")
                                entered_username = input()
                                print("Your Password")
                                entered_password = input() 

                            else:
                                print(f"Welcome {entered_username} to your Account")
                                print('\n')
                                
                                
                            while True:
                                print("Select an option below to continue:")
                                print("1: Add new credential")
                                print("2: View saved credentials")
                                print("3: Remove credential")
                                print("4: Search credential")
                                print("5: Log Out")
                                print("Enter 1, 2, 3, 4 or 5")
                                option = input()    

                                if option == '1':
                                    while True:
                                        print("Continue to add? y/n")
                                        choice = input().lower()
                                        if choice == 'y':
                                            print("Enter The Account Name")
                                            account_name = input()
                                            print("Create a password")
                                            print("You can either generate a password or create your own .To generate random password enter keyword 'genpass' or 'newpass' to create your own password")
                                            keyword = input().lower()

                                            if keyword == 'genpass':
                                                account_password = generate_password()
                                                print(f" Account: {account_name}")
                                                print(f" Password: {account_password}")
                                                print('\n')

                                            elif keyword == 'newpass':
                                                print("Create your own password")
                                                account_password = input()
                                                print(f" Account: {account_name}")
                                                print(f" Password: {account_password}")
                                                print('\n')  

                                        elif choice == 'n':
                                            print("You chose not to create an account")
                                            break
                                        else:
                                            print("Please use 'y' for yes or 'n' for no.") 

                                elif option == '2':
                                    while True:
                                        print("Here are all your credentials")
                                        if display_credentials():
                                            for credential in display_credentials():
                                                print(f"Account Name:{credential.account_name}")
                                                print(f"Password:{credential.account_password}")
                                        
                                        else:
                                            print('\n')
                                            print("You don't seem to have any credentials yet")
                                            print('\n')
                                        break    

                                elif option == '3':
                                    while True:
                                        print("Search by account name for credential you wish to delete")
                                        search_name = input()
                                        if check_existing_credentials(search_name):
                                            search_credential = find_credential(search_name)
                                            print(f"Account Name: {search_credential.account_name} \n Password: {search_credential.account_password}")
                                            print("You are about to delete {search_credential.account_name}. Are you sure you wan to delete?")
                                            response = input().lower()

                                            if response == 'y':
                                                delete_credential(search_credential)
                                                print(f"{search_credential.account_name} Your credential has been deleted")
                                                break
                                            elif response == 'n':
                                                continue
                                        else:
                                            print("Entered credential doesn't exist")

                                elif option == '4':
                                    while True:
                                        print("Enter credential name you are searching for")
                                        search_credential = input().lower()
                                        if check_existing_credentials(search_credential):
                                            search_credential = find_credential(search_credential)
                                            print(f"Account Name: {search_credential.account_name} \n Password: {search_credential.account_password}")
                                            print('\n')
                                        else:
                                            print("Entered credential doesn't exist")
                                            print("Please enter a valid code")            
                                            break

                                elif option == '5':
                                    print("Are you sure you want to log out? y/n")
                                    logout = input().lower()

                                    if logout == 'y':
                                        print("You have Successfully logged out")
                                        break
                                elif logout == 'n':
                                    continue   
        
        elif short_code == 'lg':
            print("Welcome!")
            print("Please enter Your Username")
            user_name = input()
            print("Enter Your password")
            user_password = input()
            user_exists = verify_user(user_name)

            if user_exists == user_name :
                     print(" ")
                     print (f"Welcome back {user_name} . /n Please choose an option to continue")
                     print(" ")

                     while True:
                            print("Select an option below to continue:")
                            print("1: Add new credential")
                            print("2: View saved credentials")
                            print("3: Remove credential")
                            print("4: Search credential")
                            print("5: Log Out")
                            print("Enter 1, 2, 3, 4 or 5")
                            option = input()

                            if option == '1':
                                while True:
                                    print("Continue to add? y/n")
                                    choice = input().lower()
                                    if choice == 'y':
                                        print("Enter The Account Name")
                                        account_name = input()
                                        print("Create a password")
                                        print("You can either generate a password or create your own .To generate random password enter keyword 'genpass' or 'newpass' to create your own password")
                                        keyword = input().lower()

                                        if keyword == 'genpass':
                                            account_password = generate_password()
                                            print(f" Account: {account_name}")
                                            print(f" Password: {account_password}")
                                            print('\n')

                                        elif keyword == 'newpass':
                                            print("Create your own password")
                                            account_password = input()
                                            print(f" Account: {account_name}")
                                            print(f" Password: {account_password}")
                                            print('\n')  

                                    elif choice == 'n':
                                        print("You chose not to create an account")
                                        break
                                    else:
                                        print("Please use 'y' for yes or 'n' for no.")

                            elif option == '2':
                                while True:
                                    print("Here are all your credentials")
                                    if display_credentials():
                                        for credential in display_credentials():
                                            print(f"Account Name:{credential.account_name}")
                                            print(f"Password:{credential.account_password}")
                                        
                                    else:
                                        print('\n')
                                        print("You don't seem to have any credentials yet")
                                        print('\n')
                                    break      

                            elif option == '3':
                                while True:
                                    print("Search by account name for credential you wish to delete")
                                    search_name = input()
                                    if check_existing_credentials(search_name):
                                        search_credential = find_credential(search_name)
                                        print(f"Account Name: {search_credential.account_name} \n Password: {search_credential.account_password}")
                                        print("You are about to delete {search_credential.account_name}. Are you sure you wan to delete?")
                                        response = input().lower()

                                        if response == 'y':
                                            delete_credential(search_credential)
                                            print(f"{search_credential.account_name} Your credential has been deleted")
                                            break
                                    elif response == 'n':
                                        continue
                                else:
                                    print("Entered credential doesn't exist")              

                            elif option == '4':
                                while True:
                                    print("Enter credential name you are searching for")
                                    search_credential = input().lower()
                                    if check_existing_credentials(search_credential):
                                        search_credential = find_credential(search_credential)
                                        print(f"Account Name: {search_credential.account_name} \n Password: {search_credential.account_password}")
                                        print('\n')
                                    else:
                                        print("Entered credential doesn't exist")
                                        print("Please enter a valid code")            
                                        break

                            elif option == '5':
                                print("Are you sure you want to log out? y/n")
                                logout = input().lower()

                                if logout == 'y':
                                    print("You have Successfully logged out")
                                    break
                                elif logout == 'n':
                                    continue      

        elif short_code == "ex":
            print("You are leaving")
            print('''
                                                                                     
      # ###                             ##      /                             
    /  /###  /                           ##   #/                              
   /  /  ###/                            ##   ##                              
  /  ##   ##                             ##   ##                              
 /  ###                                  ##   ##                              
##   ##            /###     /###     ### ##   ## /###   ##   ####      /##    
##   ##   ###     / ###  / / ###  / ######### ##/ ###  / ##    ###  / / ###   
##   ##  /###  / /   ###/ /   ###/ ##   ####  ##   ###/  ##     ###/ /   ###  
##   ## /  ###/ ##    ## ##    ##  ##    ##   ##    ##   ##      ## ##    ### 
##   ##/    ##  ##    ## ##    ##  ##    ##   ##    ##   ##      ## ########  
 ##  ##     #   ##    ## ##    ##  ##    ##   ##    ##   ##      ## #######   
  ## #      /   ##    ## ##    ##  ##    ##   ##    ##   ##      ## ##        
   ###     /    ##    ## ##    ##  ##    /#   ##    /#   ##      ## ####    / 
    ######/      ######   ######    ####/      ####/      #########  ######/  
      ###         ####     ####      ###        ###         #### ###  #####   
                                                                  ###         
                                                           #####   ###        
                                                         /#######  /#         
                                                        /      ###/           
                            
            ''')

            break           
                                
           
             

            
                                  






                                          



                        
                            

                           
                                
                                                         


                            

if __name__ == '__main__':
    main()                             




 
        

                            
                
                
   