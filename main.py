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
    print("Press 1 if your are a new user \nPress 2 if you are a returning user.")
    user = input("Enter:")

    if user == "1":
        username= input("Create Username:")
        password = getpass.getpass(prompt="Set/Enter a password:")
        
        print("Done!")

        dir_obj = username_dir(username)
        sha256.update(password.encode())
        hashed_passwd = sha256.hexdigest()

        write_passwd(hashed_passwd,username)


        running = False
    

    else:
        pass
