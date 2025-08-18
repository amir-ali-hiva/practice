#?

import sqlite3

query = f"SELECT * FROM a;"

with sqlite3.connect("C:/barname nevisy/programing/Python/pythonProject12/practice/practice8_5databais/data_baiss.db") as connicat:
    cursor = connicat.cursor()             #این چیکار میکنه
    results = cursor.execute(query)        #این چی کار میکنه 
rows = results.fetchall()                  #این چی کار میکنه 

for row in rows:
    print(f"Name: {row[0]}, Family: {row[1]}, Id: {row[2]}, Age: {row[3]}")

