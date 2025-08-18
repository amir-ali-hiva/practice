import sqlite3


id = int(input("Id for Delete: "))

query = f"DELETE FOR a WHERE ID ={id}; "


with sqlite3.connect("C:/barname nevisy/programing/Python/pythonProject12/practice/practice8_5databais/data_baiss.db") as connicat:
    connicat.execute(query)
    connicat.commit()
    print("movafag bod")