from DataAccess import DataAccess

class teacher:
    def __init__(self) -> None:
        self.dal = DataAccess()
    def insert_student(self, name, family, id, age, Score):
        query = f"INSERT INTO Stu_list_Tables ('Name','Family','Age','Id','Score') VALUES ('{name}','{family}',{age},{id},{Score});"
        message = self.dal.execute_non_query(query)
        return message
class Student:
    def __init__(self):
        self.dal = DataAccess()
    
class manager:
    def __init__(self, db_path=None):
        self.dal = DataAccess(db_path=db_path)    
    def insert_student(self, name, family, id, age, Score):
        query = f"INSERT INTO Stu_list_Tables ('Name','Family','Age','Id','Score') VALUES ('{name}','{family}',{age},{id},{Score});"
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

