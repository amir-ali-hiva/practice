from termcolor import colored 
import sqlite3 
n = 0
continu_e = ""
while n == 0 :#خواهستی وارد کنی وایل را حذف کن 
    id = int(input("ID of the person you want to update: "))
    name = input("Name: ")
    family = input("Family: ")
    Age  = int (input("Age: "))
    continu_e = input("Is the information correct?(yes or no)").lower()
    
    if continu_e == "yes":
        n =+ 1
    else:
        n = 0


query = f"UPDATE a SET 'Name'='{name}', 'Family'='{family}', 'Age' = '{Age}' WHERE Id = {id} "

with sqlite3.connect("C:/barname nevisy/programing/Python/pythonProject12/practice/practice8_5databais/data_baiss.db") as connicat:
    connicat.execute(query)
    connicat.commit()
print(f"{colored('Operation was sucessfull!!','green')}")