from termcolor import colored
import sqlite3

query = f"SELECT * FROM a;"

with sqlite3.connect("C:/barname nevisy/programing/Python/pythonProject12/practice/practice8_5databais/data_baiss.db") as connicat:
    cursor = connicat.cursor()               
    results = cursor.execute(query)            
rows = results.fetchall()                  

#for row in rows:
#    print(f"Name: {row[0]}, Family: {row[1]}, Id: {row[2]}, Age: {row[3]}")
conter = 0
for row in rows:
    if conter % 2 == 0:
        print(colored(f"Name: {row[0]}, Family: {row[1]}, Id: {row[2]}, Age: {row[3]}","red"))
    else:
        print(colored(f"Name: {row[0]}, Family: {row[1]}, Id: {row[2]}, Age: {row[3]}","yellow"))
    conter += 1
