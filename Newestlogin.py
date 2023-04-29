"""Gui FOr Login"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 525)
        MainWindow.setStyleSheet("border-radius{15px}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.containerThing = QtWidgets.QWidget(self.centralwidget)
        self.containerThing.setGeometry(QtCore.QRect(0, 0, 431, 531))
        self.containerThing.setStyleSheet("")
        self.containerThing.setObjectName("containerThing")
        self.label_2 = QtWidgets.QLabel(self.containerThing)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 430, 530))
        self.label_2.setStyleSheet("\n"
"background-color:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"border-radius:15px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
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
        self.User_Name_input = QtWidgets.QLineEdit(self.containerThing)
        self.User_Name_input.setGeometry(QtCore.QRect(120, 100, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(False)
        self.User_Name_input.setFont(font)
        self.User_Name_input.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(9,9,9,1);\n"
"padding-bottom:7px;")
        self.User_Name_input.setObjectName("User_Name_input")
        self.User_password_input = QtWidgets.QLineEdit(self.containerThing)
        self.User_password_input.setGeometry(QtCore.QRect(120, 160, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(False)
        self.User_password_input.setFont(font)
        self.User_password_input.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(9,9,9,1);\n"
"padding-bottom:7px;")
        self.User_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.User_password_input.setObjectName("User_password_input")
        self.Login_Button = QtWidgets.QPushButton(self.containerThing)
        self.Login_Button.setEnabled(True)
        self.Login_Button.setGeometry(QtCore.QRect(120, 230, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        self.Login_Button.setFont(font)
        self.Login_Button.setStyleSheet("Login_Button#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255)); \n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"Login_Button#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255)); \n"
"\n"
"}\n"
"Login_Button#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(9,9,9,1)\n"
"}")
        self.Login_Button.setObjectName("Login_Button")
        self.NewAccountLabel = QtWidgets.QLabel(self.containerThing)
        self.NewAccountLabel.setGeometry(QtCore.QRect(80, 300, 301, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        self.NewAccountLabel.setFont(font)
        self.NewAccountLabel.setStyleSheet("color:rgba(9,9,9,1);")
        self.NewAccountLabel.setObjectName("NewAccountLabel")
        self.NewUserNameInput = QtWidgets.QLineEdit(self.containerThing)
        self.NewUserNameInput.setGeometry(QtCore.QRect(120, 360, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(False)
        self.NewUserNameInput.setFont(font)
        self.NewUserNameInput.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(9,9,9,1);\n"
"padding-bottom:7px;")
        self.NewUserNameInput.setObjectName("NewUserNameInput")
        self.NewUserPwordInput = QtWidgets.QLineEdit(self.containerThing)
        self.NewUserPwordInput.setGeometry(QtCore.QRect(120, 420, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(False)
        self.NewUserPwordInput.setFont(font)
        self.NewUserPwordInput.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(9,9,9,1);\n"
"padding-bottom:7px;")
        self.NewUserPwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.NewUserPwordInput.setObjectName("NewUserPwordInput")
        self.CreateNewAccButton = QtWidgets.QPushButton(self.containerThing)
        self.CreateNewAccButton.setEnabled(True)
        self.CreateNewAccButton.setGeometry(QtCore.QRect(90, 480, 251, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        self.CreateNewAccButton.setFont(font)
        self.CreateNewAccButton.setStyleSheet("Login_Button#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255)); \n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"Login_Button#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255)); \n"
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
        self.User_Name_input.raise_()
        self.User_password_input.raise_()
        self.NewAccountLabel.raise_()
        self.NewUserNameInput.raise_()
        self.NewUserPwordInput.raise_()
        self.Login_Button.raise_()
        self.CreateNewAccButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PFT Login"))
        self.LoginLabel.setText(_translate("MainWindow", "Login"))
        self.User_Name_input.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.User_password_input.setPlaceholderText(_translate("MainWindow", "Password"))
        self.Login_Button.setText(_translate("MainWindow", "L o g i n"))
        self.NewAccountLabel.setText(_translate("MainWindow", "Create New Account"))
        self.NewUserNameInput.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.NewUserPwordInput.setPlaceholderText(_translate("MainWindow", "Password"))
        self.CreateNewAccButton.setText(_translate("MainWindow", "Create New Account"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())