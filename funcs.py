import os
import hashlib

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


def correct_passwd(username, passwd):
    path = f"Passwd-Manager_v2/{username}"
    file = "passwd.txt"
    os.chdir(path)

    if os.path.exists(file):
        with open(file, "rb") as f:
            real_passwd = f.read()
            



    



