from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import *
from Bussinesslogic import manager
from PyQt6.QtGui import *
from Bussinesslogic import *
from DataAccess import *
import sys
import re




class form(QWidget):
    def __init__(self):
        super().__init__()
        self.manager = manager(db_path="C:/barname nevisy/programing/Python/pythonProject12/practice/The_end/Stu_list.db")   # ساخت شیع برایه اتسال به bussinesslogic
        self.resize(600, 600)
        self.setStyleSheet("background-color: rgb( 160, 179, 96 )")
        
        self.loging()
        
        radios_layout = QGridLayout()
        main_layout = QGridLayout()
        button_layout = QGridLayout()
        tables_layout = QGridLayout()
        box_layout = QGridLayout()

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
        self.line_id.textChanged.connect(self.only_digit)
        box_layout.addWidget(self.line_id, 2, 1, 1, 1)

        label = QLabel("Age ")
        box_layout.addWidget(label, 3, 0, 1, 1)

        self.line_age = QLineEdit()
        #self.line_age.textChanged.connect(self.only_digit)
        box_layout.addWidget(self.line_age, 3, 1, 1, 1)

        label = QLabel("score")
        box_layout.addWidget(label, 4, 0, 1, 1)

        self.line_score = QLineEdit()
        #self.line_score.textChanged.connect(self.only_digit)
        #self.line_score.addItems(QColor(0,0,0))
        box_layout.addWidget(self.line_score, 4, 1, 1, 1)

        label = QLabel("Salary ")
        box_layout.addWidget(label, 5, 0, 1, 1)

        self.line_salary = QLineEdit()
        box_layout.addWidget(self.line_salary, 5, 1, 1, 1)

        label = QLabel("Time ")
        box_layout.addWidget(label, 6, 0, 1, 1)

        self.line_time = QLineEdit()
        box_layout.addWidget(self.line_time, 6, 1, 1, 1)

        label = QLabel("Filter: ")
        box_layout.addWidget(label, 7, 0, 1, 1)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["------------","Name","Family","Id","Age","Score"])
        box_layout.addWidget(self.combo_box, 7, 1, 1, 1)

        #طراحی دکمه ها

        buttel = QPushButton("Stu_list")
        buttel.clicked.connect(self.show_data)
        button_layout.addWidget(buttel, 0, 0 , 1, 1)

        buttel = QPushButton("Search")
        buttel.clicked.connect(self.search_data)
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

        buttel = QPushButton("Log in")
        buttel.clicked.connect(self.loging)
        button_layout.addWidget(buttel, 1, 3, 1, 1)

        buttel = QPushButton("Sign in")
        buttel.clicked.connect(self.sign_in)
        button_layout.addWidget(buttel, 0, 3, 1, 1)
                                                        #/////////////////////////
        buttel = QPushButton("Teacher_list")
        buttel.clicked.connect(self.teacher_list)
        button_layout.addWidget(buttel, 2, 0, 1, 1)

        buttel = QPushButton("Insert_Teacher")
        buttel.clicked.connect(self.insert_teacher)
        button_layout.addWidget(buttel, 2, 1, 1, 1)

        buttel = QPushButton("Delete_Teacher")
        buttel.clicked.connect(self.teacher_delete)
        button_layout.addWidget(buttel, 2, 2, 1, 1)

        buttel = QPushButton("Update_Teacher")
        buttel.clicked.connect(self.update_tch)
        button_layout.addWidget(buttel, 2, 3, 1, 1)

               #*******************************************************************************
        radio = QRadioButton("Starts With")
        radios_layout.addWidget(radio, 0, 0, 1, 1)

        radio = QRadioButton("Ends With")
        radios_layout.addWidget(radio, 0, 1, 1, 1)

        radio = QRadioButton("Contains")
        radios_layout.addWidget(radio, 0, 2, 1, 1)

        radio = QRadioButton("Equals")
        radios_layout.addWidget(radio, 0, 3, 1, 1)

       
        self.table = QTableView()
        self.table.setIconSize(QSize(40, 50))   # آیکن‌ها بشن 48x48
        self.table.verticalHeader().setDefaultSectionSize(35)  # ارتفاع هر ردیف 50 بشه
        self.table.doubleClicked.connect(self.show_data_topel)
        tables_layout.addWidget(self.table, 0, 0, 1, 1)


        main_layout.addLayout(box_layout, 0, 0)#bakes va laibel 
        main_layout.addLayout(button_layout, 1, 0) #دکمه
        main_layout.addLayout(tables_layout, 2, 0)  # سرچ                  سرج
        main_layout.addLayout(radios_layout, 3, 0)
        widget = QWidget()
        self.setLayout(main_layout)

    def teacher_list(self):
        try:
            self.rows = self.user.show_tch()
            if isinstance(self.rows, str):  # اگر خطا برگردوند
                QMessageBox.critical(self, "Error", self.rows)
                return
            model = Model_ch(self.rows)
            self.table.setModel(model)
            self.set_columns_width()
        except:
            pass
    def teacher_delete(self):
        try:
            id = int(self.line_id.text())                 
        
            self.message = self.user.delete_tch(id)
        
            self.teacher_list()
            self.clear_line()
            self.massege_data() 
        
        except Exception as e:
            QMessageBox.warning(self, "Delete Error", str(e))
    def insert_teacher(self):
        try:
            name = self.line_name.text()
            family = self.line_family.text()
            time = int(self.line_time.text())
            id = int(self.line_id.text())
            salary = int(self.line_salary.text())

            self.message = self.user.insert_tch(name, family, id, time, salary)
            

            self.teacher_list()
            self.clear_line()
            self.massege_data() 
        except Exception as e:
            QMessageBox.warning(self, "Insert Error", str(e))     
    def update_tch(self):
        try:
    
            id = self.line_id.text()#id = int(input("ID of the person you want to update: "))
            name = self.line_name.text()#name = input("Name: ")
            family = self.line_family.text()
            salary = int(self.line_salary.text())
            time = int(self.line_time.text())
       
            self.message = self.user.update_tch(name, family, id, salary, time)

            self.teacher_list()
            self.clear_line()
            self.massege_data()
        except Exception as e:
            QMessageBox.warning(self, "Update Error", str(e))

    def loging(self):
    #   ---------------------------------------------------------------------------------------------------------------------------
        dialog = QDialog(self)
        dialog.setWindowTitle("Login")
        dialog.resize(300, 150)

        layout = QVBoxLayout()

    
        user_label = QLabel("Select user type:")
        layout.addWidget(user_label)

        user_combo = QComboBox()
        user_combo.addItems(["Manager", "Teacher", "Student"])
        layout.addWidget(user_combo)

        username_label = QLabel("Username:")
        username_edit = QLineEdit()
        password_label = QLabel("Password:")
        password_edit = QLineEdit()
        password_edit.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(username_label)
        layout.addWidget(username_edit)
        layout.addWidget(password_label)
        layout.addWidget(password_edit)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)

        dialog.setLayout(layout)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            user_type = user_combo.currentText()

            if user_type == "Manager":
                self.user = self.manager   
                QMessageBox.information(self, "Login", "Manager login successful")

            elif user_type == "Teacher":
                self.user = teacher()      
                QMessageBox.information(self, "Login", "Teacher login successful")

            elif user_type == "Student":
                self.user = Student()
                QMessageBox.information(self, "Login", "Student login successful")
    def sign_in(self):
        QMessageBox.warning(self, "Sign in Error", str("This button belongs to God. Please log in."))
    def set_columns_width(self):
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    def show_data(self):
        try:
            self.rows = self.user.show_stu()
            if isinstance(self.rows, str):  # اگر خطا برگردوند
                QMessageBox.critical(self, "Error", self.rows)
                return
            model = Model_stu(self.rows)
            self.table.setModel(model)
            self.set_columns_width()
        except:
            pass
     
        #self.rows = self.manager.show_stu()
        #model = Model(self.rows) 
        #self.table.setModel(model)
        #self.set_columns_width()
    def search_data(self):
        try:
       
            column = self.combo_box.currentText()
            if column == "------------":
                QMessageBox.warning(self, "Search Error", "Please select a filter column")
                return

       
            match column:
                case "Id":
                    value = self.line_id.text()
                case "Name":
                    value = self.line_name.text()
                case "Family":
                    value = self.line_family.text()
                case "Age":
                    value = self.line_age.text()
                case "Score":
                    value = self.line_score.text()
                case _:
                    QMessageBox.warning(self, "Search Error", "Invalid filter selected")
                    return

  
            condition = ""
            for rb in self.findChildren(QRadioButton):
                if rb.isChecked():
                    condition = rb.text()
                    break

            if not condition:
                QMessageBox.warning(self, "Search Error", "Please select a condition")
                return

     
            self.rows = self.user.serch_stu(column, value, condition)

    
            model = Model(self.rows)
            self.table.setModel(model)
            self.set_columns_width()

        except Exception as e:
            QMessageBox.warning(self, "Search Error", str(e))
    def insert_data(self):
        try:
            name = self.line_name.text()
            family = self.line_family.text()
            age = int(self.line_age.text())
            id = int(self.line_id.text())
            score = int(self.line_score.text())

            self.message = self.user.insert_student(name, family, id, age, score)
            

            self.show_data()
            self.clear_line()
            self.massege_data() 
        except Exception as e:
            QMessageBox.warning(self, "Insert Error", str(e))          
    def update_data(self):
        try:
    
            id = self.line_id.text()#id = int(input("ID of the person you want to update: "))
            name = self.line_name.text()#name = input("Name: ")
            family = self.line_family.text()
            age = int(self.line_age.text())
            score = int(self.line_score.text())
       
            self.message = self.user.update_stu(name, family, id, age, score)

            self.show_data()
            self.clear_line()
            self.massege_data()
        except Exception as e:
            QMessageBox.warning(self, "Update Error", str(e))
    def delete_data(self):
        try:
            id = int(self.line_id.text())                 #id = int(input("Id for delete: "))
        
            self.message = self.user.delete_stu(id)
        
            self.show_data()
            self.clear_line()
            self.massege_data() 
        
        except Exception as e:#       e  متن خطاییه که خود پایتون میده
            QMessageBox.warning(self, "Delete Error", str(e))
    def exit_form(self):
        result = QMessageBox.question(self,
            "Exit!!!!!???",
            "Are you sure you want to exit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if result == QMessageBox.StandardButton.Yes:
            
            QApplication.quit() #این روش تمیزتر از exit()
    
    def show_data_topel(self, index):
        row_index = index.row()
        self.line_id.setText(str(self.rows[row_index][0]))
        self.line_name.setText(str(self.rows[row_index][1]))
        self.line_family.setText(str(self.rows[row_index][2]))
        self.line_age.setText(str(self.rows[row_index][3]))
        self.line_score.setText(str(self.rows[row_index][4]))


    def clear_line(self):
        self.line_name.setText("")
        self.line_family.setText("")
        self.line_age.setText("")
        self.line_id.setText("")
        self.line_score.setText("")
        self.line_salary.setText("")
        self.line_time.setText("")

    def massege_data(self):
        msg_box = QMessageBox()
        msg_box.setText(self.message)
        msg_box.exec()

    def only_digit(self, line):
        new_text = re.sub("[^0-9]", "", line)
        self.line_id.setText(new_text)
        #self.line_age.setText(new_text)
        #self.line_score.setText(new_text)       

class Model_stu(QAbstractTableModel):
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

    def data(self, index: QModelIndex, role: int = ...):    # پردازش روی داده ها
        value = f"{self.rows[index.row()][index.column()]}"
        if role == Qt.ItemDataRole.DisplayRole:                     
            return value
        

        if role == Qt.ItemDataRole.DecorationRole:
            if index.column() == 4:   # ستون Score
                score = int(self.rows[index.row()][index.column()])
                if score >= 70:                   #***********************************/چرا کار نمیکنه\*****************************
                    return QIcon("C:/barname nevisy/programing/Python/pythonProject12/practice/The_end/accept.png")
                else:
                    return QIcon("C:/barname nevisy/programing/Python/pythonProject12/practice/The_end/rejected.png")


            
        if role == Qt.ItemDataRole.BackgroundRole:  #color for backgrond tabels
            if index.row() % 2 == 0:
                return QColor(139, 147, 255)
            else:
                return QColor(255, 113, 205)
            
        if role == Qt.ItemDataRole.ForegroundRole:  # color tabels txet
            if index.row() % 2 == 0:
                return QColor(84, 18, 18)
            else:
                return QColor(30, 3, 66)
            
        if role == Qt.ItemDataRole.TextAlignmentRole:  # اگر هدفت وسط چین متن بود
            return Qt.AlignmentFlag.AlignCenter
        
        if role == Qt.ItemDataRole.FontRole:              #  font txet    
            return QFont("Arial", 10, 8, italic=False)
            
    def rowCount(self, parent: QModelIndex = ...) :          
        return len(self.rows)      #len اندازه را میده
    
    def columnCount(self, parent: QModelIndex = ...):        
        return len(self.rows[0])
class Model_ch(QAbstractTableModel):
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
                        return "Salary"
                    case 4:
                        return "Time Class"
            if orientation == Qt.Orientation.Vertical:
                return section + 1

    def data(self, index: QModelIndex, role: int = ...):    # پردازش روی داده ها
        value = f"{self.rows[index.row()][index.column()]}"
        if role == Qt.ItemDataRole.DisplayRole:                     
            return value
        

        if role == Qt.ItemDataRole.DecorationRole:
            if index.column() == 4:   # ستون Score
                score = int(self.rows[index.row()][index.column()])
                if 90 >= 70:                   #***********************************/چرا کار نمیکنه\*****************************
                    return QIcon("C:/barname nevisy/programing/Python/pythonProject12/practice/The_end/teacher.png")


            
        if role == Qt.ItemDataRole.BackgroundRole:  #color for backgrond tabels
            if index.row() % 2 == 0:
                return QColor(139, 147, 255)
            else:
                return QColor(255, 113, 205)
            
        if role == Qt.ItemDataRole.ForegroundRole:  # color tabels txet
            if index.row() % 2 == 0:
                return QColor(84, 18, 18)
            else:
                return QColor(30, 3, 66)
            
        if role == Qt.ItemDataRole.TextAlignmentRole:  # اگر هدفت وسط چین متن بود
            return Qt.AlignmentFlag.AlignCenter
        
        if role == Qt.ItemDataRole.FontRole:              #  font txet    
            return QFont("Arial", 10, 8, italic=False)
            
    def rowCount(self, parent: QModelIndex = ...) :          
        return len(self.rows)      #len اندازه را میده
    
    def columnCount(self, parent: QModelIndex = ...):        
        return len(self.rows[0])
    

app = QApplication(sys.argv)
form = form()
form.show()
sys.exit(app.exec())