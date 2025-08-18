import sqlite3

name = input("Name: ")
family = input("Family: ")
id = int (input("Id: "))
age = int(input("Age: "))


query = f"INSERT INTO a ('Name','Family','Id','Age')\
      VALUES ('{name}', '{family}', {id}, {age})"
connection = sqlite3.connect("C:/barname nevisy/programing/Python/pythonProject12/practice/practice8_5databais/data_baiss.db")
connection.execute(query)
connection.commit()
connection.close()