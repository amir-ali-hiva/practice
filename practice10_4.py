from termcolor import colored
import sqlite3

query = f"SELECT * FROM a;"

with sqlite3.connect("C:/barname nevisy/programing/Python/pythonPr\
oject12/practice/practice8_5databais/data_baiss.db") as connicat:    
    cursor = connicat.cursor()               
    results = cursor.execute(query)            
rows = results.fetchall()                  


for i ,row in enumerate(rows):
    color = "red" if i % 2 == 0  else "yellow"  
    print(colored(f"Name: {row[0]}, Family: {row[1]}, Id: {row[2]}, Age: {row[3]}",color))