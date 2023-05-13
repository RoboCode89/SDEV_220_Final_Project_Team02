#import of all needed libraries and widgets
import sys
import csv
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QAction, QHeaderView, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout,QFileDialog,)
from PyQt5.QtGui import QPainter, QStandardItemModel
from PyQt5.Qt import Qt                                            
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5 import QtWidgets



class DataEntryForm(QWidget):            #adding views to the main window object
    def __init__(self):
        super().__init__()

        #checks how many items are in the table
        self.items = 0

       
        #left side of the app screen setup, 2 columns, header names Description and Price
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(("Description", "Price"))
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #auto exapnd column width
        
        # Add label above table
        self.layoutTable = QVBoxLayout()
        self.label = QLabel("Double click a description or price to edit")
        self.layoutTable.addWidget(self.label)
        self.layoutTable.addWidget(self.table)

        #create layout object for with 50% of screen used
        self.layout = QHBoxLayout()
        self.layout.addLayout(self.layoutTable, 50)

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

        # Add label above table
        self.layoutTable = QVBoxLayout()
        self.label = QLabel("Double click a description or price to edit")
        self.layoutTable.addWidget(self.label)
        self.layoutTable.addWidget(self.table)


        #create layout object for with 50% of screen used
        self.layout = QHBoxLayout()
        self.layout.addLayout(self.layoutTable, 50)
        self.layout.addLayout(self.layoutRight, 50)

#creates layout object for buttons to sit in, connects buttons to functions
        app = QApplication(sys.argv)
        self.setLayout(self.layout)
        self.buttonQuit.clicked.connect(lambda:app.quit())
        self.buttonClear.clicked.connect(self.reset_table)
        self.buttonPlot.clicked.connect(self.graph_chart)          
        self.buttonAdd.clicked.connect(lambda: self.add_entry())

#connects input fields, specifices string and adds functions
        self.LineEditDescription.textChanged[str].connect(self.check_disable)
        self.lineEditPrice.textChanged[str].connect(self.check_disable)
        

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
    def add_entry(self, desc=None, price=None):
        print('add_entry called')
        print(f"desc: {desc}")
        print(f"price: {price}")
        if desc is None and price is None:
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
    
    #function for saving file
    def save_data(self):
        #get file name and filter it for CSV
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Save Data", "", "CSV Files (*.csv)"
        )
        if fileName:
            with open(fileName, "w") as file: #open file in write mode
                writer = csv.writer(file)
                #writing the data rows
                for row in range(self.table.rowCount()):
                    desc = self.table.item(row, 0).text()
                    price = self.table.item(row, 1).text()
                    writer.writerow([desc, price])
   
   
    #function for loading file from saved location or create new
    def load_data(self):
        QtWidgets.QMessageBox.information(None, "Choose a CSV file", 'Load A CSV file from saved, Or choose Cancel To Create New')
        #getting file name and filtering for csv files
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Load Data", "", "CSV Files (*.csv)"
        )
        if fileName:
            #opening file in read
            with open(fileName, "r") as file:
                reader = csv.reader(file)
                next(reader) #skipping over header rows in table
                for row in reader:
                    desc, price = row
                    self.add_entry(desc, float(price.replace("$", "")))#add new entry while removing $ before converting to float
       



class MainWindow(QMainWindow):                                                                         #application main interface class
    def __init__(self, w):
        super().__init__()
        self.DataEntryForm = w   #--------
        app = QApplication(sys.argv)  #------test
        #print('Initializing mainwindow')  testing purpose                                                                           #inheirt 
        self.setWindowTitle('Expense Data Entry Form')                                                 #window title
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


    #function for csv files
    def export_to_csv(self):
        #get file name and filter it for csv files
        fileName,_ = QFileDialog.getSaveFileName(self, "Export to CSV", "", "CSV Files (*.csv)")
        if fileName:
            try:
                with open(fileName, "w", newline="") as file: #opeing file in write mode
                    writer = csv.writer(file)
                    #writing header row
                    writer.writerow(
                        (
                            self.DataEntryForm.table.horizontalHeaderItem(0).text(),
                            self.DataEntryForm.table.horizontalHeaderItem(1).text(),
                        )
                    )
                    #writing data rows
                    for rowNumber in range(self.DataEntryForm.table.rowCount()):
                        writer.writerow(
                            [
                                self.DataEntryForm.table.item(rowNumber, 0).text(),
                                self.DataEntryForm.table.item(rowNumber, 1).text(),
                            ]
                        )
                
            except Exception as e:
                print(e)
        
    

# initializing Pythons interpreter to read source files and define few special variables/global variables
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DataEntryForm()
    w.load_data()
    app.aboutToQuit.connect(w.save_data)
    main = MainWindow(w)
    main.show()

    sys.exit(app.exec_())