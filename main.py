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
    user = input("Please press y if you are a new user ,But if you are a returning user press n:")

    if user == "Y" or user == "y":
        username= input("Create Username:")
        password = p = getpass.getpass(prompt="Set/Enter a password:")
        
        print("Done!")

        dir_obj = username_dir(username)
        sha256.update(password.encode())
        hashed_passwd = sha256.hexdigest()

        write_passwd(hashed_passwd,dir_obj)

        

        running = False
    

    
    else:
        pass
