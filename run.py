#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
from pyfiglet import Figlet
import randon
import string
import pyperclip

def create_user( user_name, email, password):
	'''
	function to create new user
	'''
	new_user = User(user_name, email, password)
	return new_user


def save_user(self):
	'''
	Method that saves User
	'''
	User.save_user("self")



def delete_user(self):
	'''
	Function that deletes user
	'''
	User.delete_user()

        
def find_user(email, password):
	'''
	Function that finds user when one choses to log in.
	'''
	return  User.find_user(email, password)


def check_existing_user(user):
    '''
    Function that checks for existing Users
    '''
    return User.check_existing_user(user)

    
def display_users():
	'''
	function that saves Users
	'''
	return User.display_users()

def new_credentials(account_name, login_detail , Password):
 	new_credentials(save_credentials)

def create_credentials(account_name, login_detail , Password):

    new_credentials = Credentials(account_name, login_detail , Password)
    return new_credentials
        




def save_credentials():
	'''
	methods that saves credentials.
	'''
	return Credentials.save_credentials()

	

def create_credentials( save_credentials):
	'''
	function to create new user
	'''
	Credentials.create_credentials("account_name", "login_detail" , "Password")
	

def copy_User_credential():
	'''
	Function that copies cridentials on clipboard
	'''
	return User.find_user(email)
pyperclip.copy(user_found.email)

def passGen(size = 8, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    gen = ''.join(random.choice(char) for _ in range(size))
    return gen
