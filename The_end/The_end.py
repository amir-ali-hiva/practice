from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from Bussinesslogic import manager
from Bussinesslogic import *
from DataAccess import *
import sys
import sqlite3

class form(QWidget):
    def __init__(self):
        super().__init__()
        self.manager = manager()   # ساخت شیع برایه اتسال به bussinesslogic
        self.resize(500, 500)
        #self.setStyleSheet("background-color: rgb( 232 , 2 , 163 )")
        

        main_layout = QGridLayout()
        box_layout = QGridLayout()
        button_layout = QGridLayout()
        tables_layout = QGridLayout()

        #label and box
        label = QLabel("Name ")
        box_layout.addWidget(label, 0, 0, 1, 1)

        self.line_name = QLineEdit()
        box_layout.addWidget(self.line_name, 0, 1, 1, 1)


        label = QLabel("Family ")
        box_layout.addWidget(label, 1, 0, 1, 1)

        self.line_family = QLineEdit()
        box_layout.addWidget(self.line_family, 1, 1, 1, 1)

        label = QLabel("Id ")
        box_layout.addWidget(label, 2, 0, 1, 1)

        self.line_id = QLineEdit()
        box_layout.addWidget(self.line_id, 2, 1, 1, 1)

        label = QLabel("Age ")
        box_layout.addWidget(label, 3, 0, 1, 1)

        self.line_age = QLineEdit()
        box_layout.addWidget(self.line_age, 3, 1, 1, 1)

        label = QLabel("Score ")
        box_layout.addWidget(label, 4, 0, 1, 1)

        self.line_Score = QLineEdit()
        box_layout.addWidget(self.line_Score, 4, 1, 1, 1)

        #طراحی دکمه ها
        buttel = QPushButton("Show all")
        button_layout.addWidget(buttel, 0, 0 , 1, 1)

        buttel = QPushButton("Search")
        button_layout.addWidget(buttel, 0, 1 , 1, 1)

        buttel = QPushButton("Insert")
        buttel.clicked.connect(self.insert_data)
        button_layout.addWidget(buttel, 0, 2 , 1, 1)

        buttel = QPushButton("Update")
        buttel.clicked.connect(self.update_data)
        button_layout.addWidget(buttel, 1, 0 , 1, 1)

        buttel = QPushButton("Delete")
        buttel.clicked.connect(self.delete_data)
        button_layout.addWidget(buttel, 1, 1 , 1, 1)

        buttel = QPushButton("Exit")
        buttel.clicked.connect(self.exit_form)
        button_layout.addWidget(buttel, 1, 2 , 1, 1)

        tables = QTableView()

        tables_layout.addWidget(tables, 0, 0, 1, 1)

        main_layout.addLayout(box_layout, 0, 0)#bakes va laibel 
        main_layout.addLayout(button_layout, 1, 0) #دکمه
        main_layout.addLayout(tables_layout, 2, 0)

        self.setLayout(main_layout)
    def show_data(self):
        pass
    def search_data(self):
        pass
    def insert_data(self):

             
        name = self.line_name.text()
        family = self.line_family.text()
        age = int(self.line_age.text())
        id = int(self.line_id.text())
        Score = int(self.line_Score.text())

        message = self.manager.insert_student(name, family, id, age, Score)
            

        self.show_data()
        self.clear_line()
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.exec()
        
            
            #msg_box = QMessageBox()
            #msg_box.setText(message)
            #msg_box.exec()
    def update_data(self):
        pass
    def delete_data(self):
        pass
    def exit_form(self):
        result = QMessageBox.question(self,
            "Exit!!!!!???",
            "Are you sure you want to exit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if result == QMessageBox.StandardButton.Yes:
            
            QApplication.quit() #این روش تمیزتر از exit()
    

    def clear_line(self):
        self.line_name.setText("")
        self.line_family.setText("")
        self.line_age.setText("")
        self.line_id.setText("")
        self.line_Score.setText("")
           

app = QApplication(sys.argv)
form = form()
form.show()
sys.exit(app.exec())