
class User():
    def __init__(self, userName, userPassword):
        self.userName = userName
        self.userPassword = userPassword

def Register():
    userName = input("Username: ")
    userPassword = input("Password: ")

    with open("register.txt", "r") as file:
        for name in file:
            if userName in name:
                print("Username already exists.")
                return

    with open("register.txt", "a") as file:
        file.write(userName + '/' + userPassword + "\n")

Register()



def userLogin():
    userName = input("Username: ")
    userPassword = input("Password: ")

    with open("register.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            items = line.strip().split('/')
            if items[0] == userName and items[1] == userPassword:
                print("Login Success")                
                break
        else:
            print("Login Failed")
userLogin()

   

    
    


