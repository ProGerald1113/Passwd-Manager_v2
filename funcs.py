import os

def username_dir(username):
    
    path = username
    os.mkdir(path)

def write_passwd(passwd,parent_dir):
    parent_dir = parent_dir
    filename = "hashed_passwd.txt"
    file_path = os.path.join(parent_dir,filename)
    with open(file_path, "wb") as file:
        file.write(passwd)


