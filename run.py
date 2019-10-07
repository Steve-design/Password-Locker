#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

import random
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
	User.delete_user(self)

        
def find_user(user_name, password):
	'''
	Function that finds user when one choses to log in.
	'''
	return  User.find(user_name, password)


def check_existing_user(self):
    '''
    Function that checks for existing Users
    '''
    return User.check_existing_user(self)

    
def display_users(self):
	'''
	function that saves Users
	'''
	return User.display_users(self)

# def new_credentials(account_name, login_detail , Password):
#  	new_credentials(create_credentials)

def create_credentials(account_name, login_detail , Password):

    new_credentials = Credentials(account_name, login_detail , Password)
    return new_credentials
        




def save_credentials(self):
	'''
	methods that saves credentials.
	'''
	return Credentials.credentials_list.append(self)

def copy_User_credential():
	'''
	Function that copies cridentials on clipboard
	'''
	return User.find_user(email)


def passGen(size = 8, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    gen = ''.join(random.choice(char) for _ in range(size))
    return gen

def main():

	
	

	print("Welcome to Password Locker. Your safety is our priority. Check through the content then enter the shortcode to navigate:\n sign ---- to sign up,\n log ----   to log In,\n  exit ---- to exit ")
	
	
	print("*" *80)
	
	code = input().lower()
	
	if code == "log": 
			
		print("Enter your  Username")
		user_name = input().lower()

		print ("Enter your password")
		password = input()
		
		if find_user(user_name, password) == password: 
			print("Successfully logged in")	
	

		else:
			print("The details you gave do not match any account. Please enter the codes to Sign up and enjoy our services.")
			
			code = input()


	elif code == "sign":
		print("Enter your details to create new account")
		print("Enter Username")
		user_name = input().lower()

		print("Enter your email adress")
		email = input().lower()

		print("Enter your password")
		password = input()
		save_user(create_user( user_name, email, password))

		print(f"Welcome {user_name} to Password Locker. You are now logged in.")
		print("\n")
		
		print("Use the following codes to proceed :\n create - create new account details,\n display - display accounts,\n exit - exit the Application")
		while True:
			code = input()
			if code == "create":
				print("Please enter the Account details for the password you want to save: ")
				print("Account name")
				account = input()
				print("LogIn details used.eg. phone number,email ")
				email = input()
				print ("Enter 1 to input a password, to have one automatically generated for you enter 2.")
				
				password_choice = input()

				
				if password_choice == "1":
					password = print(input("enter your password"))
					print(password)
					
				
				elif password_choice == "2":
					password = passGen()
					print(password)

				
				else:
					print("Please input shortcode 1 or 2.")
					
					
				
				save_credentials(create_credentials(account,email,password))

				print(f"You have successfully added an account with the following details\nAccount name: {account}\nLog in details used: {email}\nPassword: {password}.")
				print("You can now create another account type in create,to display accounts created type display,to exit type exit")
				
			elif code == "display":

				save_user(create_user(user_name, email, password)) 

				print ("\n")
				print(f"A new user,with a user name {user_name} and email {email} has been added")
				
				print("Bingo!, kindly use the given codes to proceed")


		
	elif code =="exit":
		        print("Logging Out ...")

		        print("\n")	
		        print("Enjoy the rest of your day. Asante!")




	else:
		print("Dear customer,you have entered invalid codes. Kindly enter the following  codes to access Password Locker:\n sign - Sign Up,")


if __name__ == '__main__':
    main()  
