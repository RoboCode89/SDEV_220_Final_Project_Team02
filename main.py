""""Test Main with a capital MMMMMMMMMM"""
import sys
import csv
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QAction, QHeaderView, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QPainter, QStandardItemModel, QIcon
from PyQt5.Qt import Qt                                            
from PyQt5.QtChart import QChart, QChartView, QPieSeries
#from cryptography.fernet import Fernet         


class DataEntryForm(QWidget):            #adding views to the main window object
    def __init__(self):
        super().__init__()

        #checks how many items are in the table
        self.items = 0

        #dummy data set for examples, dictionary
        self._data = {"Double click a description or price to edit": 0.0, "Gas": 30.0, "rent": 1850.0, "Car Payment": 420.0, 
                      "Entertainment": 105.0, "Public Transport": 60.0, "Coffee":90.5}

        #left side of the app screen setup, 2 columns, header names Description and Price
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(("Description", "Price"))
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #auto exapnd column width

        #create layout object
        self.layoutRight = QVBoxLayout()

        # set chart widget using a render method in Qpainter for better resolution
        self.chartView = QChartView()                         
        self.chartView.setRenderHint(QPainter.Antialiasing)
        

        #create widgets options for container (input lines for description and price Add Clear Quit Plot buttons)
        self.LineEditDescription = QLineEdit()
        self.lineEditPrice = QLineEdit()
        self.buttonAdd = QPushButton("Add")
        self.buttonClear = QPushButton("Clear")
        self.buttonQuit = QPushButton("Quit")
        self.buttonPlot = QPushButton("Plot")

        #add button requires input to trigger
        self.buttonAdd.setEnabled(False)

        #add widgets to layout container (laid out in order of apperence)
        self.layoutRight.setSpacing(10)
        self.layoutRight.addWidget(QLabel("Description"))
        self.layoutRight.addWidget(self.LineEditDescription)
        self.layoutRight.addWidget(QLabel("Price"))
        self.layoutRight.addWidget(self.lineEditPrice)
        self.layoutRight.addWidget(self.buttonAdd)
        self.layoutRight.addWidget(self.buttonPlot)
        self.layoutRight.addWidget(self.chartView)     
        self.layoutRight.addWidget(self.buttonClear)
        self.layoutRight.addWidget(self.buttonQuit)

        #create layout object for with 50% of screen used
        self.layout = QHBoxLayout()    
        self.layout.addWidget(self.table, 50)
        self.layout.addLayout(self.layoutRight, 50)

#creates layout object for buttons to sit in, connects buttons to functions
        self.setLayout(self.layout)
        self.buttonQuit.clicked.connect(lambda:app.quit())
        self.buttonClear.clicked.connect(self.reset_table)
        self.buttonPlot.clicked.connect(self.graph_chart)          
        self.buttonAdd.clicked.connect(self.add_entry)

#connects input fields, specifices string and adds functions
        self.LineEditDescription.textChanged[str].connect(self.check_disable)
        self.lineEditPrice.textChanged[str].connect(self.check_disable)

        #popluat fill records in table widget
        self.fill_table()

    #populate the dummy data if there is no data present to display, 
    def fill_table(self, data=None):
        data = self._data if not data else data                      #if there is data this will load it instead

        #formating for display
        for desc, price in data.items():
            descItem = QTableWidgetItem(desc)
            priceItem = QTableWidgetItem('${0:.2f}'.format(price))
            priceItem.setTextAlignment(Qt.AlignRight | Qt.AlignCenter)      

            #update counter self.items and add new row index
            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, descItem)
            self.table.setItem(self.items, 1, priceItem)
            self.items += 1

#Gets description and price from user input feild, adds to the table then clears the line, ValueError checked for input verification price must be int/float
    def add_entry(self):
        desc = self.LineEditDescription.text()
        price = self.lineEditPrice.text()

        try: 
            descItem = QTableWidgetItem(desc)
            priceItem = QTableWidgetItem('${0:.2f}'.format(float(price)))
            priceItem.setTextAlignment(Qt.AlignRight | Qt.AlignCenter)       

            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, descItem)
            self.table.setItem(self.items, 1, priceItem)
            self.items += 1
        except ValueError:
            pass

#empty strings to clear the input after adding
        self.LineEditDescription.setText("")
        self.lineEditPrice.setText("")

#checks of there are values in input, enabling or disabeling the add button updating the boolean value
    def check_disable(self):
        if self.LineEditDescription.text() and self.lineEditPrice.text():
            self.buttonAdd.setEnabled(True)
        else:
            self.buttonAdd.setEnabled(False)

#clears the chart
    def reset_table(self):
        self.table.setRowCount(0)
        self.items = 0

        chart = QChart()                       
        self.chartView.setChart(chart)

#creates pie chart with QpieSeries
    def graph_chart(self):                   
        series = QPieSeries()
#populates table row data converts strings to floats updates $ to blank space
        for i in range(self.table.rowCount()):
            text = self.table.item(i, 0).text()
            val = float(self.table.item(i,1).text().replace("$", ''))
            series.append(text, val)
#adds for loop info into chart
        chart = QChart()
        chart.addSeries(series)
        chart.legend().setAlignment(Qt.AlignTop)
        self.chartView.setChart(chart)





class MainWindow(QMainWindow):                                                                         #application main interface class
    def __init__(self, w):
        super().__init__()
        self.DataEntryForm = w   #--------
        print('Initializing mainwindow')                                                                             #inheirt 
        self.setWindowTitle('Expense Data Entry Form')                                                 #window title
        #self.setWindowIcon(QIcon(r'C:\Users\peglo\OneDrive\SDEV220\Project stuff\financial_icon.png')) #set file path for icon png file, needs to adjust once file uplaod
        self.resize(1200,600)                                                                          #size of window

        self.menuBar = self.menuBar()                                                                  #set menu bar 
        self.fileMenu = self.menuBar.addMenu('File')                                                   #set menu bar name

        #export to CSV file action in menu bar, linking function "export_to_csv"
        exportAction = QAction("Export to CSV", self)
        exportAction.setShortcut('Ctrl+E')
        exportAction.triggered.connect(self.export_to_csv)            

        #exit action in menu bar
        exitAction = QAction('Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(lambda:app.quit())

        #addd to the file menu actions
        self.fileMenu.addAction(exportAction)
        self.fileMenu.addAction(exitAction)

        #pass the widget object to mainwindow
        self.setCentralWidget(w) 



#---------------------------------------------New process to encrypt CSV file----- NOT FINISHED----
    # def encryptCSV():
    #     #key generation
    #     key = Fernet.generate_key()

    #     # string the key in a file
    #     with open('filekey.key','wb') as filekey:
    #         filekey.write(key)

    #     #opening the key
    #     with open('filekey.key', 'rb') as filekey:
    #         key = filekey.read()
        
    #     with open ('Expense Report.csv', 'rb') as file:
    #         original = file.read()

    #     encrypted = Fernet.encrypt(original)

    #     with open ('Expense Report.csv', 'wb') as encrypted_file:
    #         encrypted_file.write(encrypted)

    

#---------------------------------------------New process to encrypt CSV file----- NOT FINISHED----






#self.DataEntryForm ------ w
    #function to export CSV file, using csv module, file saved as Expense Report.csv, file opened and closed.
    def export_to_csv(self):
        try:
            with open('Expense Report.csv','w', newline='' ) as file:
                writer = csv.writer(file)
                writer.writerow((self.DataEntryForm.table.horizontalHeaderItem(0).text(), self.DataEntryForm.table.horizontalHeaderItem(1).text()))
                for rowNumber in range(w.table.rowCount()):
                    writer.writerow([self.DataEntryForm.table.item(rowNumber, 0).text(), self.DataEntryForm.table.item(rowNumber, 1).text()])

                print('CSV file exported')
                file.close()
        except Exception as e:
            print(e)
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DataEntryForm()
    main = MainWindow(w)
    main.show()

    sys.exit(app.exec_())