# import of necessary libraries
import hashlib #importing hashing for encryption/decryption
from PyQt5 import QtWidgets


#user class to define username and pw
class User():
    def init(self, userName, userPassword):
        self.userName = userName
        #hashing the pw / used sha256 algorithm to has because it is supported by all systems
        #.encode turns pw to bytes and hexdigest turns the bytes to a hexadecimal number
        self.userPassword =hashlib.sha256(userPassword.encode()).hexdigest()

#function for user registration
def Register(NewUserName, NewUserPassword):
    userName = NewUserName
    userPassword = NewUserPassword
    #checking if username is already in use
    with open("register.txt", "r") as file:
        for name in file:
            if userName in name:
                QtWidgets.QMessageBox.warning(None, 'Error', 'Username already exists')
                return
    #writing the username and pw to file
    with open("register.txt", "a") as file: #"a"=append credentials to end of text file
        file.write(userName + '/' + hashlib.sha256(userPassword.encode()).hexdigest() + "\n")

    QtWidgets.QMessageBox.information(None, 'Congratulations!', 'Registration Successful')

#function for user login
def userLogin(userName, userPassword): 
    print('in login function')#backend testing purpose
    userName = userName
    userPassword = userPassword
    login_successful = False
    #reading file for username and pw and if it matches they login if not says failed.
    with open("register.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            items = line.strip().split('/')           
             #checking if username matches what is stored in file and if the hashed pw matches           
            if items[0] == userName and items[1] == hashlib.sha256(userPassword.encode()).hexdigest():
                    login_successful = True
                    break
    if login_successful:
        print('login successful')
        #QtWidgets.QMessageBox.information(None, 'Welcome', 'Login Successful!')
                
        return login_successful           
        

    else:        
        QtWidgets.QMessageBox.warning(None, 'Error', 'Invalid Login')
                    
            
               