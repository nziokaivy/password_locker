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
