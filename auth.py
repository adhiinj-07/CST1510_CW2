import bcrypt
from pathlib import Path
PATH=Path(__file__).parent / 'DATA' /  'user.txt'

def hash_password(password:str):
    binary_password=password.encode("utf-8")
    salt=bcrypt.gensalt()
    hash=bcrypt.hashpw(binary_password,salt)
    return hash.decode('utf-8')


def is_valid_password(password:str,hash:str):
    check_password=bcrypt.checkpw(password.encode('utf-8'),hash.encode('utf-8'))
    return check_password

def register_user(username:str,password:str):
    hash=hash_password(password)
    with open(PATH,"a") as file:
        file.write(f"{username},{hash}\n")
        print(f"user{username}registered successfully.")
def login_user(username:str,password:str):
    with open(PATH,"r") as f:
        for line in f:
            user,hash=line.strip().split(",")
            if user==username:
                if is_valid_password(password,hash):
                    print(f"User {username} logged in successfully.")
                    return True
                else:
                    print("invalid password")
                    return False


if __name__=="__main__":
    while True:
        choice=input("enter(1) to register:or (2) to login : (3to exit)")
        if choice =="1":
            user_name=input("enter your username")
            password=input("enter password")
            register_user(user_name,password)
            
        elif choice=="2":
            user_name=input("enter your username")
            password=input("enter password")
            if login_user(user_name,password):
                print("login successful")
            else:
                print("incorrect username or password")   

        elif choice=="3":
            break

    
    
    
    
    