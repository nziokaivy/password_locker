#!/usr/bin/env python3.6

import random
from password import Account_user
from credentials import Credential

def create_new_credential(account_name, account_password):
    """
    Function to create a new account and its credentials
    """
    new_credential = Credential(account_name, account_password)
    return new_credential

def save_new_credential(credentials):
    """
    Function to save the newly created account and password
    """
    credentials.save_credentials()

def find_credential(account_name):
    """
    Function that finds credentials using the account_name provided
    """
    return Credential.find_by_name(account_name)

def check_existing_credentials(name):
    """
    Function that checks whether a particular account and its credentials exist when searched using the account_name"""
    return Credential.find_by_name(name)  

def delete_credential(credentials):
    """
    Function that deletes credentials
    """
    return Credential.delete_credential(credentials)


def display_credentials():
    """
    Function which displays all saved credentials
    """
    return Credential.display_credentials()  

def main():

    while True:
        print("Welcome to Password Locker.")
        print('\n')
        print("Use these short codes to select an option: Create New User use 'cu': Login to your account use 'lg' or 'ex' to exit password locker")
        short_code = input().lower()
        print('\n')

        if short_code == 'cu':
            print("Create a username")
            created_user_name = input()
            print("Select a Password")
            created_user_password = input()


            while confirm_password != created_user_password:
                print("Sorry you entered the wrong password!")
                print("Enter a password")
                created_user_password = input()

            else:
                print(f"Congratulations {created_user_name}! You have a new account!.")
                print('\n')
                print("You can now log In to your Account")
                print("Username")
                entered_userName = input()
                print("Your Password")
                entered_password = input()

            while entered_userName != created_user_name or entered_password != created_user_password:
                    print("You entered a wrong username or password")
                    print("Username")
                    entered_userName = input()
                    print("Your Password")
                    entered_password = input()    

            else:
                    print(f"Welcome: {entered_userName} to your Account")
                    print('\n')

                    print("Select an option below to continue: Enter 1, 2, 3, 4 or 5")
                    print('\n')

            while True:
                    print("1: Add new credential")
                    print("2: View saved credentials")
                    print("3: Remove credential")
                    print("4: Search credential")
                    print("5: Log Out")
                    option = input()

                    if option == '1':
                        while True:
                            print("Continue to add? y/n")

                            choice = input().lower()
                            if choice == 'y':
                                print("Enter The Account Name")
                                account_name = input()
                                print("Enter a password")
                                print(
                                    "To generate random password enter keyword 'genpass' or 'newpass' to create your own password")
                                keyword = input().lower()

                                if keyword == 'gp':
                                    account_password = generate_password()
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')

                                elif keyword == 'n':
                                    print("Create your password")
                                    account_password = input()
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')

                            elif choice == 'n':
                                break
                            else:
                                print("Please use 'y' for yes or 'n' for no!")

                    
    
                
                
   