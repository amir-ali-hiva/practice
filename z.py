from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sqlite3
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
                        return "Name"
                    case 1:
                        return "Family"
                    case 2:
                        return "Id"
                    case 3:
                        return "Age"
            if orientation == Qt.Orientation.Vertical:
                return section + 1

    def data(self, index: QModelIndex, role: int = ...):            # پردازش روی داده ها
        value = f"{self.rows[index.row()][index.column()]}"
        if role == Qt.ItemDataRole.DisplayRole:                     # اگر هدفت نمایش داده بود
            return value
        
        if role == Qt.ItemDataRole.DecorationRole:                  # اگر هدفت گذاشتن آیکون بود
            if str(value).lower() in ["hamid", "alireza", "amir", "ali"]:
                return QIcon("1.png")
            
        if role == Qt.ItemDataRole.BackgroundRole:                  # اگر هدفت تغییر رنگ بک گراند بود
            if index.row() % 2 == 0:
                return QColor(129, 236, 236)
            else:
                return QColor(232, 67, 147)
            
        if role == Qt.ItemDataRole.ForegroundRole:                  # اگر هدفت تغییر رنگ متن بود
            if str(value).lower() == "hamid":
                return QColor("blue")
            
        if role == Qt.ItemDataRole.TextAlignmentRole:               # اگر هدفت تراز متن بود
            return Qt.AlignmentFlag.AlignCenter
        
        if role == Qt.ItemDataRole.FontRole:                        # اگر هدفت تغییر فونت باشد
            if str(value).lower() == "hamid":
                return QFont("cursive", 12, 4, italic=True)
            
    def rowCount(self, parent: QModelIndex = ...) -> int:           # باید تعداد سطرها را بدهد
        return len(self.rows)
    
    def columnCount(self, parent: QModelIndex = ...) -> int:        # باید تعداد ستون ها را بدهد
        return len(self.rows[0])

class Form(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(500, 500)
        # self.setStyleSheet("background-color: rgb(232,67,147);")

        main_layout = QGridLayout()
        boxes_layout = QGridLayout()
        radios_layout = QGridLayout()
        buttons_layout = QGridLayout()
        tables_layout = QGridLayout()

        #region Boxes
        label = QLabel("Name: ")
        boxes_layout.addWidget(label, 0, 0, 1, 1)

        self.txt_name = QLineEdit()
        boxes_layout.addWidget(self.txt_name, 0, 1, 1, 1)

        label = QLabel("Family: ")
        boxes_layout.addWidget(label, 1, 0, 1, 1)

        self.txt_family = QLineEdit()
        boxes_layout.addWidget(self.txt_family, 1, 1, 1, 1)

        label = QLabel("Id: ")
        boxes_layout.addWidget(label, 2, 0, 1, 1)

        self.txt_id = QLineEdit()
        boxes_layout.addWidget(self.txt_id, 2, 1, 1, 1)

        label = QLabel("Age: ")
        boxes_layout.addWidget(label, 3, 0, 1, 1)

        self.txt_age = QLineEdit()
        boxes_layout.addWidget(self.txt_age, 3, 1, 1, 1)

        label = QLabel("Filter: ")
        boxes_layout.addWidget(label, 4, 0, 1, 1)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["----------","Name","Family","Id","Age"])
        boxes_layout.addWidget(self.combo_box, 4, 1, 1, 1)
        #endregion

        #region Buttons
        button = QPushButton("Select")
        button.clicked.connect(self.select_info)
        buttons_layout.addWidget(button, 0, 0, 1, 1)

        button = QPushButton("Search")
        button.clicked.connect(self.search_info)
        buttons_layout.addWidget(button, 0, 1, 1, 1)

        button = QPushButton("Insert")
        button.clicked.connect(self.insert_info)
        buttons_layout.addWidget(button, 0, 2, 1, 1)

        button = QPushButton("Update")
        button.clicked.connect(self.update_info)
        buttons_layout.addWidget(button, 0, 3, 1, 1)

        button = QPushButton("Delete")
        button.clicked.connect(self.delete_info)
        buttons_layout.addWidget(button, 0, 4, 1, 1)

        button = QPushButton("Close")
        button.clicked.connect(self.close_form)
        buttons_layout.addWidget(button, 0, 5, 1, 1)
        #endregion

        #region Radios
        radio = QRadioButton("Starts With")
        radios_layout.addWidget(radio, 0, 0, 1, 1)

        radio = QRadioButton("Ends With")
        radios_layout.addWidget(radio, 0, 1, 1, 1)

        radio = QRadioButton("Contains")
        radios_layout.addWidget(radio, 0, 2, 1, 1)

        radio = QRadioButton("Equals")
        radios_layout.addWidget(radio, 0, 3, 1, 1)
        #endregion

        self.table = QTableView()
        self.table.doubleClicked.connect(self.show_data)
        tables_layout.addWidget(self.table, 0, 0, 1, 1)

        main_layout.addLayout(boxes_layout, 0, 0)
        main_layout.addLayout(radios_layout, 1, 0)
        main_layout.addLayout(buttons_layout, 2, 0)
        main_layout.addLayout(tables_layout, 3, 0)

        self.setLayout(main_layout)

    def select_info(self):
        query = "SELECT * FROM TBLStudents;"
        with sqlite3.connect("DBStudents.db") as connection:
            cursor = connection.cursor()
            results = cursor.execute(query)
        self.rows = results.fetchall()
        model = Model(self.rows)
        self.table.setModel(model)
        self.set_columns_width()

    def search_info(self):
        try:
            filter_number = "0" # input("[0:Name, 1:Family, 2:Age, 3:Id]: ")
            condition_number = "0" # input("[0:Starts With, 1: Ends With, 2: Contains, 3:Equals]: ")

            query = f"SELECT * FROM TBLStudents Where"
            match filter_number:
                case "0":
                    filter = "Name"
                    value = self.txt_name.text()
                case "1":
                    filter = "Family"
                    value = self.txt_family.text()
                case "2":
                    filter = "Age"
                    value = self.txt_age.text()
                case "3":
                    filter = "Id"
                    value = self.txt_id.text()
                case _:
                    # Show Message Box
                    return

            match condition_number:
                case "0":
                    query = f"{query} {filter} LIKE '{value}%'"
                case "1":
                    query = f"{query} {filter} LIKE '%{value}'"
                case "2":
                    query = f"{query} {filter} LIKE '%{value}%'"
                case "3":
                    if filter in ["Age", "Id"]:
                        query = f"{query} {filter} = {value}"
                    else:
                        query = f"{query} {filter} = '{value}'"
                case _:
                    # show message box
                    return
            
            with sqlite3.connect("DBStudents.db") as connection:
                cursor = connection.cursor()
                results = cursor.execute(query)
                self.rows = results.fetchall()
            model = Model(self.rows)
            self.table.setModel(model)
            self.set_columns_width()
                
        except:
            print(colored("Error was occurred!!!", "red"))

    def insert_info(self):
        try:
            name = self.txt_name.text()     # input("Name: ")
            family = self.txt_family.text()
            age = int(self.txt_age.text())
            id = int(self.txt_id.text())

            query = f"INSERT INTO TBLStudents ('Name','Family','Age','Id') VALUES ('{name}','{family}',{age},{id})"
            with sqlite3.connect("DBStudents.db") as connection:
                connection.execute(query)
                connection.commit()

            self.select_info()
            self.clear_boxes()

            msg_box = QMessageBox()
            msg_box.setText("Operation was successfull!!!")
            msg_box.exec()
        except:
            msg_box = QMessageBox()
            msg_box.setText("Error was Occured!!!")
            msg_box.exec()

    def update_info(self):
        try:
            name = self.txt_name.text()
            family = self.txt_family.text()
            age = int(self.txt_age.text())
            id = int(self.txt_id.text())

            query = f"UPDATE TBLStudents SET Name='{name}', \
                    Family='{family}', Age={age} WHERE Id={id};"

            with sqlite3.connect("dbStudents.db") as connection:
                connection.execute(query)
                connection.commit()

            self.select_info()
            self.clear_boxes()

            msg_box = QMessageBox()
            msg_box.setText("Operation was successfull!!!!")
            msg_box.exec()
        except:
            msg_box = QMessageBox()
            msg_box.setText("Error was Occured!!!")
            msg_box.exec()

    def delete_info(self):
        try:
            id = int(self.txt_id.text())

            query = f"DELETE FROM TBLStudents WHERE Id={id}"

            with sqlite3.connect("DBStudents.db") as connection:
                connection.execute(query)
                connection.commit()

            self.select_info()
            self.clear_boxes()

            msg_box = QMessageBox()
            msg_box.setText("Operation was successful!!!")
            msg_box.exec()
        except:
            msg_box = QMessageBox()
            msg_box.setText("Error was occurred!!!")
            msg_box.exec()

    def close_form(self):
        self.close()

    def show_data(self, index):
        row_index = index.row()
        self.txt_name.setText(str(self.rows[row_index][0]))
        self.txt_family.setText(str(self.rows[row_index][1]))
        self.txt_id.setText(str(self.rows[row_index][2]))
        self.txt_age.setText(str(self.rows[row_index][3]))

    def clear_boxes(self):
        self.txt_name.setText("")
        self.txt_family.setText("")
        self.txt_age.setText("")
        self.txt_id.setText("")

    def set_columns_width(self):
        width = self.table.width()
        for i in range(4):
            self.table.setColumnWidth(i, width // 4 - 11)

app = QApplication(sys.argv)
form = Form()
form.show()
sys.exit(app.exec())