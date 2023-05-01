import hashlib #importing hashing
#user class to define username and pw
class User():
    def __init__(self, userName, userPassword):
        self.userName = userName
        #hashing the pw / used sha256 algorithm to has because it is supported by all systems
        #.encode turns pw to bytes and hexdigest turns the bytes to a hexadecimal number
        self.userPassword =hashlib.sha256(userPassword.encode()).hexdigest()
#function for user registration
def Register():
    userName = input("Username: ")
    userPassword = input("Password: ")
    #checking if username is already in use
    with open("register.txt", "r") as file:
        for name in file:
            if userName in name:
                print("Username already exists.")
                return
    #writing the username and pw to file
    with open("register.txt", "a") as file: #"a"=append credentials to end of text file
        file.write(userName + '/' + hashlib.sha256(userPassword.encode()).hexdigest() + "\n")
#running function to test
Register()


#function for user login
def userLogin():
    userName = input("Username: ")
    userPassword = input("Password: ")
    #reading file for username and pw and if it matches they login if not says failed.
    with open("register.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            items = line.strip().split('/')
            #checking if username matches what is stored in file and if the hashed pw matches
            if items[0] == userName and items[1] == hashlib.sha256(userPassword.encode()).hexdigest():
                print("Login Success") #sample output               
                break
        else:
            print("Login Failed") #sample output
#running function to test            
userLogin()

   

    
    


