from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from Bussinesslogic import manager
from Bussinesslogic import *
from DataAccess import *
import sys


class Model(QAbstractTableModel):
    def __init__(self, rows) -> None:
        super().__init__()
        self.rows = rows

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                match section:
                    case 0:
                        return "Id"
                    case 1:
                        return "Name"
                    case 2:
                        return "Family"
                    case 3:
                        return "Age"
                    case 4:
                        return "Score"
            if orientation == Qt.Orientation.Vertical:
                return section + 1

    def data(self, index: QModelIndex, role: int = ...):            # پردازش روی داده ها
        value = f"{self.rows[index.row()][index.column()]}"
        if role == Qt.ItemDataRole.DisplayRole:                     # اگر هدفت نمایش داده بود
            return value
        
        #if role == Qt.ItemDataRole.DecorationRole:                  # اگر هدفت گذاشتن آیکون بود
        #    if str(value).lower() in ["hamid", "alireza", "amir", "ali"]:
        #        return QIcon("1.png")
            
        #if role == Qt.ItemDataRole.BackgroundRole:                  # اگر هدفت تغییر رنگ بک گراند بود
        #    if index.row() % 2 == 0:
        #        return QColor(129, 236, 236)
        #    else:
        #        return QColor(232, 67, 147)
            
        #if role == Qt.ItemDataRole.ForegroundRole:                  # اگر هدفت تغییر رنگ متن بود
        #    if str(value).lower() == "hamid":
        #        return QColor("blue")
            
        if role == Qt.ItemDataRole.TextAlignmentRole:               # اگر هدفت تراز متن بود
            return Qt.AlignmentFlag.AlignCenter
        
        #if role == Qt.ItemDataRole.FontRole:                        # اگر هدفت تغییر فونت باشد
        #    if str(value).lower() == "hamid":
        #        return QFont("cursive", 12, 4, italic=True)
            
    def rowCount(self, parent: QModelIndex = ...) -> int:           # باید تعداد سطرها را بدهد
        return len(self.rows)
    
    def columnCount(self, parent: QModelIndex = ...) -> int:        # باید تعداد ستون ها را بدهد
        return len(self.rows[0])


class form(QWidget):
    def __init__(self):
        super().__init__()
        self.manager = manager(db_path="C:/barname nevisy/programing/Python/pythonProject12/practice/The_end/Stu_list.db")   # ساخت شیع برایه اتسال به bussinesslogic
        self.resize(500, 500)
        self.setStyleSheet("background-color: rgb( 160, 179, 96 )")
        

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

        label = QLabel("score ")
        box_layout.addWidget(label, 4, 0, 1, 1)

        self.line_score = QLineEdit()
        box_layout.addWidget(self.line_score, 4, 1, 1, 1)

        #طراحی دکمه ها
        buttel = QPushButton("Show all")
        buttel.clicked.connect(self.show_data)
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
     
        self.rows = self.manager.show_stu()


       
        model = Model(self.rows)
        
        self.table.setModel(model)
        self.set_columns_width()
    def search_data(self):
        pass
    def insert_data(self):
        try:
            name = self.line_name.text()
            family = self.line_family.text()
            age = int(self.line_age.text())
            id = int(self.line_id.text())
            score = int(self.line_score.text())

            self.message = self.manager.insert_student(name, family, id, age, score)
            

            self.show_data()
            self.clear_line()
            self.massege_data() 
        except:
            pass           
    def update_data(self):
        try:
    
            id = self.line_id.text()#id = int(input("ID of the person you want to update: "))
            name = self.line_name.text()#name = input("Name: ")
            family = self.line_family.text()
            age = int(self.line_age.text())
            score = int(self.line_score.text())
       
            self.message = self.manager.update_stu(name, family, id, age, score)

            self.show_data()
            self.clear_line()
            self.massege_data()
        except:
            pass
    def delete_data(self):
        try:
            id = int(self.line_id.text())                 #id = int(input("Id for delete: "))
        
            self.message = self.manager.delete_stu(id)
        
            self.show_data()
            self.clear_line()
            self.massege_data() 
        
        except:
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
        self.line_score.setText("")

    def massege_data(self):
        msg_box = QMessageBox()
        msg_box.setText(self.message)
        msg_box.exec()       

app = QApplication(sys.argv)
form = form()
form.show()
sys.exit(app.exec())