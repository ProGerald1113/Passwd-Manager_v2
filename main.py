from cryptography.fernet import Fernet 
from funcs import username_dir
import getpass
import os 


key = Fernet.generate_key()

f = Fernet(key)



running = True

while running:
    print("Welcome to your password manager!")
    print("Are you a returning user or a new user?")
    user = input("Please press y if you are a new user ,But if you are a returning user press n:")

    if user == "Y" or user == "y":
        username= input("Create Username:")
        password = p = getpass.getpass(prompt="Set/Enter a password:")
        username_dir(username)

        running = False
    

    
    else:
        pass
