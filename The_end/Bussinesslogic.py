from DataAccess import DataAccess

class teacher:
    def __init__(self, db_path="C:/barname nevisy/programing/Python/pythonProject12/practice/The_end/Stu_list.db"):
        self.dal = DataAccess(db_path=db_path) 
    def serch_stu(self, column, value, condition):
        query = f"SELECT * FROM Stu_list_Tables WHERE "
        match condition:
            case "Starts With":
                query += f"{column} LIKE '{value}%'"
            case "Ends With":
                query += f"{column} LIKE '%{value}'"
            case "Contains":
                query += f"{column} LIKE '%{value}%'"
            case "Equals":
                if column in ["Id", "Age", "Score"]:
                    query += f"{column} = {value}"
                else:
                    query += f"{column} = '{value}'"
        result = self.dal.execute_query(query)
        return result
    def delete_stu(self, id):
        query = f"DELETE FROM Stu_list_Tables WHERE Id={id}"
        message = self.dal.execute_non_query(query)
        return message
    def show_stu(self):
        query = "SELECT * FROM Stu_list_Tables;"
        message = self.dal.execute_query(query)
        return message
    def update_stu(self, name, family, id, age, score):
        query =  f"UPDATE Stu_list_Tables SET 'Name'='{name}', 'Family'='{family}','Score'='{score}' ,'Age' = '{age}' WHERE Id = {id}; "
        message = self.dal.execute_non_query(query)
        return message
    def insert_student(self, name, family, id, age, score):
        message = "You must tell the manager to insert ."
        return message 
    def delete_tch(self, id):
        message = "You must tell the manager to delete ."
        return message  
    def show_tch(self):
        query = "SELECT * FROM Teacher_list_Tables;"
        message = self.dal.execute_query(query)
        return message  
    def insert_tch(self, name, family, id, time, salary):
        message = "You must tell the manager to insert ."
        return message
    def update_tch(self, name, family, id, time, salary):
        message = "You must tell the manager to update ."
        return message    
class manager:
    def __init__(self, db_path="C:/barname nevisy/programing/Python/pythonProject12/practice/The_end/Stu_list.db"):
        self.dal = DataAccess(db_path=db_path)    
    def insert_student(self, name, family, id, age, score):
        query = f"INSERT INTO Stu_list_Tables ('Name','Family','Age','Id','Score') VALUES ('{name}','{family}',{age},{id},{score});"
        message = self.dal.execute_non_query(query)
        return message
    def delete_stu(self, id):
        query = f"DELETE FROM Stu_list_Tables WHERE Id={id}"
        message = self.dal.execute_non_query(query)
        return message
    def show_stu(self):
        query = "SELECT * FROM Stu_list_Tables;"
        message = self.dal.execute_query(query)
        return message
    def update_stu(self, name, family, id, age, score):
        query =  f"UPDATE Stu_list_Tables SET 'Name'='{name}', 'Family'='{family}','Score'='{score}' ,'Age' = '{age}' WHERE Id = {id}; "
        message = self.dal.execute_non_query(query)
        return message  
    def serch_stu(self, column, value, condition):
        query = f"SELECT * FROM Stu_list_Tables WHERE "
        match condition:
            case "Starts With":
                query += f"{column} LIKE '{value}%'"
            case "Ends With":
                query += f"{column} LIKE '%{value}'"
            case "Contains":
                query += f"{column} LIKE '%{value}%'"
            case "Equals":
                if column in ["Id", "Age", "Score"]:
                    query += f"{column} = {value}"
                else:
                    query += f"{column} = '{value}'"
        result = self.dal.execute_query(query)
        return result
    def delete_tch(self, id):
        query = f"DELETE FROM Teacher_list_Tables WHERE Id={id}"
        message = self.dal.execute_non_query(query)
        return message
    def show_tch(self):
        query = "SELECT * FROM Teacher_list_Tables;"
        message = self.dal.execute_query(query)
        return message
    def insert_tch(self, name, family, id, time, salary):
        query = f"INSERT INTO Teacher_list_Tables ('Name','Family','Id','Salary','Time Class') VALUES ('{name}','{family}',{id},{salary},{time});"
        message = self.dal.execute_non_query(query)
        return message
    def update_tch(self, name, family, id, time, salary):
        query =  f"UPDATE Teacher_list_Tables SET 'Name'='{name}', 'Family'='{family}','Time Class'='{time}' ,'Salary' = '{salary}' WHERE Id = {id}; "
        message = self.dal.execute_non_query(query)
        return message  
class Student:
    def __init__(self, db_path="C:/barname nevisy/programing/Python/pythonProject12/practice/The_end/Stu_list.db"):
        self.dal = DataAccess(db_path=db_path)
    def serch_stu(self, column, value, condition):
        query = f"SELECT * FROM Stu_list_Tables WHERE "
        match condition:
            case "Starts With":
                query += f"{column} LIKE '{value}%'"
            case "Ends With":
                query += f"{column} LIKE '%{value}'"
            case "Contains":
                query += f"{column} LIKE '%{value}%'"
            case "Equals":
                if column in ["Id", "Age", "Score"]:
                    query += f"{column} = {value}"
                else:
                    query += f"{column} = '{value}'"
        result = self.dal.execute_query(query)
        return result 
    def show_stu(self):
        query = "SELECT * FROM Stu_list_Tables;"
        message = self.dal.execute_query(query)
        return message
    def insert_student(self, name, family, id, age, score):
        message = "You must tell the manager to insert ."
        return message 
    def delete_stu(self, id):
        message = "You must tell the manager to delete ."
        return message 
    def update_stu(self, name, family, id, age, score):
        message = "You must tell the teacher to update ."
        return message
    def show_tch(self):
        message = "This panel is not designed for students!!!"
        return message 
    def delete_tch(self):
        message = "This panel is not designed for students!!!"
        return message 
    def update_tch(self):
        message = "This panel is not designed for students!!!"
        return message 
    def insert_tch(self):
        message = "This panel is not designed for students!!!"
        return message 
      
        