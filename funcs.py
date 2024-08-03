import os

def username_dir(username):
    path = username
    os.mkdir(path)

def write_passwd(passwd,username):

    path = f"/Passwd-Manager_v2/{username}"
    print(path)

    if os.path.exists(path):
        with open("hashed_passwd.txt","ab+") as file:
            file.write(passwd.encode())
    
    else:
        pass

username = "gee12"
username_dir(username)
write_passwd("njafkjs",username)

