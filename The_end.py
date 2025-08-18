from PyQt6.QtWidgets import *
import sys
import os

class form(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        #self.setStyleSheet("background-color: rgb( 232 , 2 , 163 )")
        def closeEvent(self, event):
            self.exit_form

        main_layout = QGridLayout()
        box_layout = QGridLayout()
        button_layout = QGridLayout()
        tables_layout = QGridLayout()

        #label and box
        label = QLabel("Name ")
        box_layout.addWidget(label, 0, 0, 1, 1)

        line = QLineEdit()
        box_layout.addWidget(line, 0, 1, 1, 1)


        label = QLabel("Family ")
        box_layout.addWidget(label, 1, 0, 1, 1)

        line = QLineEdit()
        box_layout.addWidget(line, 1, 1, 1, 1)

        label = QLabel("Id ")
        box_layout.addWidget(label, 2, 0, 1, 1)

        line = QLineEdit()
        box_layout.addWidget(line, 2, 1, 1, 1)

        label = QLabel("Age ")
        box_layout.addWidget(label, 3, 0, 1, 1)

        line = QLineEdit()
        box_layout.addWidget(line, 3, 1, 1, 1)

        #طراحی دکمه ها
        buttel = QPushButton("Show all")
        button_layout.addWidget(buttel, 0, 0 , 1, 1)

        buttel = QPushButton("Search")
        button_layout.addWidget(buttel, 0, 1 , 1, 1)

        buttel = QPushButton("Insert")
        button_layout.addWidget(buttel, 0, 2 , 1, 1)

        buttel = QPushButton("Update")
        button_layout.addWidget(buttel, 1, 0 , 1, 1)

        buttel = QPushButton("Delete")
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
        pass
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

        

app = QApplication(sys.argv)
form = form()
form.show()
sys.exit(app.exec())