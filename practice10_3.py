from termcolor import colored
import sqlite3

query = f"SELECT * FROM a;"

with sqlite3.connect("C:/barname nevisy/programing/Python/pythonProject12/practice/practice8_5databais/data_baiss.db") as connicat:
    cursor = connicat.cursor()               
    results = cursor.execute(query)            
rows = results.fetchall()                  

#for row in rows:
 #   print(f"Name: {row[0]}, Family: {row[1]}, Id: {row[2]}, Age: {row[3]}")
#conter = 0
#for row in rows:
#    if conter % 2 == 0:
#        print(colored(f"Name: {row[0]}, Family: {row[1]}, Id: {row[2]}, Age: {row[3]}","red"))
#    else:
#        print(colored(f"Name: {row[0]}, Family: {row[1]}, Id: {row[2]}, Age: {row[3]}","yellow"))
#    conter += 1
#for i in range(len(rows)):
#    if i % 2 == 0:
#        print(colored(f"Name: {rows[i][0]}, Family: {rows[i][1]}, Id: {rows[i][2]}, Age: {rows[i][3]}","red"))
#    else:
#        print(colored(f"Name: {rows[i][0]}, Family: {rows[i][1]}, Id: {rows[i][2]}, Age: {rows[i][3]}","yellow"))
#for i, row in enumerate(rows):
#    if i % 2 == 0:
#        print(colored(f"Name: {row[0]}, Family: {row[1]}, Id: {row[2]}, Age: {row[3]}","red"))
#    else:
#        print(colored(f"Name: {row[0]}, Family: {row[1]}, Id: {row[2]}, Age: {row[3]}","yellow"))
for i ,row in enumerate(rows):
    color = "red" if i % 2 == 0  else "yellow"  
    print(colored(f"Name: {row[0]}, Family: {row[1]}, Id: {row[2]}, Age: {row[3]}",color))