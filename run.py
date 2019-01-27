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
    Method that checks whether a particular account and its credentials exist when searched using the account_name"""
    return Credential.find_by_name(name)  

def delete_credential(credentials):
    """
    Method that deletes credentials
    """
    return Credential.delete_credential(credentials)


def display_credentials():
    """
    Function which displays all saved credentials
    """
    return Credential.display_credentials()    


   