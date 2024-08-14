from cryptography.fernet import Fernet 
from funcs import *
import getpass
import os 
import hashlib

sha256 = hashlib.sha256()

key = Fernet.generate_key()

f = Fernet(key)

running = True

while running:

    print("Welcome to your password manager!")
    print("Are you a returning user or a new user?")
    
    print("----------------------------------------------------------------------------------------------------")
    
    print("Press 1 if your are a new user \nPress 2 if you are a returning user.\nPress 3 to quit.")
    
    user = input("Enter:")


    if user == "1":
        username= input("Create Username:")
        password = getpass.getpass(prompt="Set/Enter a password:")
        
        print("Done!")


        write_passwd(password,username)


    elif user == "2":
        
        username_check = input("Enter your username:")
        correct_user(username_check)
        
        passwd_check = input("Enter your password:")
        passwd_correct(passwd_check)
    
    elif user == "3":
        print("Thanks for using the password manager v2 please come again")
        running = False
