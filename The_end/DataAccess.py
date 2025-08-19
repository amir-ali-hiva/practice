
import sqlite3

class DataAccess:
    def __init__(self):
        self.db_path = "Stu_list.db"
        self.db_path = db_path
    

    def execute_query(self,query):
        try:
            with sqlite3.connect(self.db_path) as conection:
                curose = conection.cursor()
                result = curose.execute(query)
            rows = result.fetchall()
            

        except Exception as error:
            rows = f"Error!! {error}"
        return rows
    
    def execute_non_query(self,query):

        try:            
            with sqlite3.connect(self.db_path) as connection:
                connection.execute(query)
                connection.commit()
            message = "Operation Was Successfull!!!"

        except Exception as error:
            message = f"Error!! {error}"     
        return message
