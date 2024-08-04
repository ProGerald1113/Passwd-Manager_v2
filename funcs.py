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


def correct_or_not(username, passwd):
    
    sha256.update(passwd.encode())
    passwd = sha256.hexdigest()


    Correct = True

    path = f"home/browngerald2008/Passwd-Manager_v2/{username}"

    file = "passwd.txt"
    os.chdir(path)

    with open(file, "rb") as f:
        real_passwd = f.read()
    
    if real_passwd != passwd or not os.path.exists(path):
        print("One or both of the details you entered are wrong please double check")

    else:
        print("Correct!")

correct_or_not("Gee", "Gee")

    



