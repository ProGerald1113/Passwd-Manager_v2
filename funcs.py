import os
import hashlib
import sys


sha256 = hashlib.sha256()

def username_dir(username):
    path = username
    os.mkdir(path)

def write_passwd(passwd,username):

    sha256.update(passwd.encode())
    
    username_dir(username)

    hashed_passwd = sha256.hexdigest()

    folder = f"{username}"
    file = "passwd.txt"

    file_path = os.path.join(folder,file) 


    if os.path.exists(folder):
        with open(file_path,"w") as file:
            file.write(str(hashed_passwd))
    
    else:
        print("error")


def correct_user(username):
    
    path = f"/home/browngerald2008/Passwd-Manager_v2/{username}"
    
    os.chdir(path)
    
    if os.path.exists(path):
        print("This user exists")
        print("----------------------------------------------------------------------------------------------------")
    
    else:
        print("Incorrect!!!!")
        print("----------------------------------------------------------------------------------------------------")
        sys.exit()
        
def passwd_correct(passwd):
    
    file = "passwd.txt"
    sha256 = hashlib.sha256()
    
    sha256.update(passwd.encode())
    
    hashed_passwd = sha256.hexdigest()
    
    with open(file, "r") as file:
        real_passwd = file.read()
        
    if real_passwd == hashed_passwd:
        print("Your password is correct!")
        print("----------------------------------------------------------------------------------------------------")

        
    else:
        print("ITS WRONG!")
        print("----------------------------------------------------------------------------------------------------")

        sys.exit()
    
        