
class User():
    def __init__(self, userName, userPassword):
        self.userName = userName
        self.userPassword = userPassword
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
        file.write(userName + '/' + userPassword + "\n")
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
            if items[0] == userName and items[1] == userPassword:
                print("Login Success") #sample output               
                break
        else:
            print("Login Failed") #sample output
#running function to test            
userLogin()

   

    
    


