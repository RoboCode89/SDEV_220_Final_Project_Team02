"""Gui FOr Login
code set to .setStyleSheet is CSS code for display"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from userLOGIN import *

# creates main window to pass container object into
class Ui_MainWindow(object):

    #adds each object from .Ui file setup from Qtdesigner program
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 525)
        MainWindow.setStyleSheet("border-radius{15px}")
        
        #Could break without, not to sure if its needed...
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        #inner container that holds all objects
        self.containerThing = QtWidgets.QWidget(self.centralwidget)
        self.containerThing.setGeometry(QtCore.QRect(0, 0, 431, 531))
        self.containerThing.setStyleSheet("")
        self.containerThing.setObjectName("containerThing")

        #background that hass CSS for yellow effect
        self.label_2 = QtWidgets.QLabel(self.containerThing)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 430, 530))
        self.label_2.setStyleSheet("background-color:qconicalgradient(cx:0, cy:0, angle:135,\n"
                                "stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69),\n"
                                "stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208),\n"
                                "stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130),\n"
                                "stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69),\n"
                                "stop:1 rgba(255, 255, 0, 69));\n"
                                "border-radius:15px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        # displays the "Login" text
        self.LoginLabel = QtWidgets.QLabel(self.containerThing)
        self.LoginLabel.setGeometry(QtCore.QRect(160, 40, 111, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        self.LoginLabel.setFont(font)
        self.LoginLabel.setStyleSheet("color:rgba(9,9,9,1);")
        self.LoginLabel.setObjectName("LoginLabel")

        # -------------------------------------------------------------------------------user input for "GuiUserName"... Need to get info for login
        self.GuiUserName = QtWidgets.QLineEdit(self.containerThing)
        self.GuiUserName.setGeometry(QtCore.QRect(120, 100, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(False)
        self.GuiUserName.setFont(font)
        self.GuiUserName.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                        "border:none;\n"
                                        "border-bottom:2px solid rgba(105,118,132,255);\n"
                                        "color:rgba(9,9,9,1);\n"
                                        "padding-bottom:7px;")
        self.GuiUserName.setObjectName("GuiUserName")

        #---------------------------------------------------------------------------------user input for "GuiUserPassword ... Need to get info for login
        self.GuiUserPassword = QtWidgets.QLineEdit(self.containerThing)
        self.GuiUserPassword.setGeometry(QtCore.QRect(120, 160, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(False)
        self.GuiUserPassword.setFont(font)
        self.GuiUserPassword.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                                "border:none;\n"
                                                "border-bottom:2px solid rgba(105,118,132,255);\n"
                                                "color:rgba(9,9,9,1);\n"
                                                "padding-bottom:7px;")
        self.GuiUserPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.GuiUserPassword.setObjectName("GuiUserPassword")

        #---------------------------------------------------------------------------------login button.. need linked button to function for user authentication
        self.Login_Button = QtWidgets.QPushButton(self.containerThing)
        self.Login_Button.setEnabled(True)
        self.Login_Button.setGeometry(QtCore.QRect(120, 230, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        self.Login_Button.setFont(font)
        self.Login_Button.setStyleSheet("Login_Button#pushButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255),\n"
                                        "stop:1 rgba(255, 255, 255, 255)); \n"
                                        "color:rgba(255,255,255,210);\n"
                                        "border-radius:5px;\n"
                                        "}\n"
                                        "\n"
                                        "Login_Button#pushButton:hover{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255)); \n"
                                        "\n"
                                        "}\n"
                                        "Login_Button#pushButton:pressed{\n"
                                        "padding-left:5px;\n"
                                        "padding-top:5px;\n"
                                        "background-color:rgba(9,9,9,1)\n"
                                        "}")
        self.Login_Button.setObjectName("Login_Button")
        




        #label text for "New User"
        self.NewAccountLabel = QtWidgets.QLabel(self.containerThing)
        self.NewAccountLabel.setGeometry(QtCore.QRect(110, 300, 301, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        self.NewAccountLabel.setFont(font)
        self.NewAccountLabel.setStyleSheet("color:rgba(9,9,9,1);")
        self.NewAccountLabel.setObjectName("NewAccountLabel")

        #-------------------------------------------------------------------------------------- Feild for "GuiNewUserName"... Need to get info for login Reg new user
        self.GuiNewUserName = QtWidgets.QLineEdit(self.containerThing)
        self.GuiNewUserName.setGeometry(QtCore.QRect(120, 360, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(False)
        self.GuiNewUserName.setFont(font)
        self.GuiNewUserName.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                                "border:none;\n"
                                                "border-bottom:2px solid rgba(105,118,132,255);\n"
                                                "color:rgba(9,9,9,1);\n"
                                                "padding-bottom:7px;")
        self.GuiNewUserName.setObjectName("GuiNewUserName")

        #------------------------------------------------------------------------------ Feild for "GuiNewUserPassword" ... Need to get info for login Reg new user pword
        self.GuiNewUserPassword = QtWidgets.QLineEdit(self.containerThing)
        self.GuiNewUserPassword.setGeometry(QtCore.QRect(120, 420, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(False)
        self.GuiNewUserPassword.setFont(font)
        self.GuiNewUserPassword.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                                "border:none;\n"
                                                "border-bottom:2px solid rgba(105,118,132,255);\n"
                                                "color:rgba(9,9,9,1);\n"
                                                "padding-bottom:7px;")
        self.GuiNewUserPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.GuiNewUserPassword.setObjectName("GuiNewUserPassword")

        #---------------------------------------------------------------------------------------------button for creating new user... need function from login 
        self.CreateNewAccButton = QtWidgets.QPushButton(self.containerThing)
        self.CreateNewAccButton.setEnabled(True)
        self.CreateNewAccButton.setGeometry(QtCore.QRect(90, 480, 251, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        self.CreateNewAccButton.setFont(font)
        self.CreateNewAccButton.setStyleSheet("Login_Button#pushButton{\n"
                                                " background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255),\n"
                                                "stop:1 rgba(255, 255, 255, 255)); \n"
                                                "color:rgba(255,255,255,210);\n"
                                                "border-radius:5px;\n"
                                                "}\n"
                                                "\n"
                                                "Login_Button#pushButton:hover{\n"
                                                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255),\n"
                                                "stop:1 rgba(255, 255, 255, 255)); \n"
                                                "\n"
                                                "}\n"
                                                "Login_Button#pushButton:pressed{\n"
                                                "    padding-left:5px;\n"
                                                "    padding-top:5px;\n"
                                                "    background-color:rgba(9,9,9,1)\n"
                                                "}")
        self.CreateNewAccButton.setObjectName("CreateNewAccButton")


        self.label_2.raise_()
        self.LoginLabel.raise_()
        self.GuiUserName.raise_()
        self.GuiUserPassword.raise_()
        self.NewAccountLabel.raise_()
        self.GuiNewUserName.raise_()
        self.GuiNewUserPassword.raise_()
        self.Login_Button.raise_()
        self.CreateNewAccButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #translation from .Ui file created from Qtdesigner
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PFT Login"))
        self.LoginLabel.setText(_translate("MainWindow", "Login"))
        self.GuiUserName.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.GuiUserPassword.setPlaceholderText(_translate("MainWindow", "Password"))
        self.Login_Button.setText(_translate("MainWindow", "L o g i n"))
        self.NewAccountLabel.setText(_translate("MainWindow", "New Account"))
        self.GuiNewUserName.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.GuiNewUserPassword.setPlaceholderText(_translate("MainWindow", "Password"))
        self.CreateNewAccButton.setText(_translate("MainWindow", "Create New Account"))

       
#----------------------------------------------------------------------------------------------Buttons connected to functions
        self.Login_Button.clicked.connect(self.getUserInfo)
        self.CreateNewAccButton.clicked.connect(self.getNewUserInfo)
 
    def getUserInfo(self):
        userName = self.GuiUserName.text()
        userPassword = self.GuiUserPassword.text()
        print(userName, userPassword)
        userLogin(userName, userPassword)


    def getNewUserInfo(self):
        NewUserName = self.GuiNewUserName.text()
        NewUserPassword = self.GuiNewUserPassword.text()
        print(NewUserName,NewUserPassword)
        Register(NewUserName,NewUserPassword)






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
