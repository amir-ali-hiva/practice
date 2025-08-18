import sqlite3

id = int(input("Id for delete: "))


query = f"DELETE FROM a WHERE ID = {id};"


with sqlite3.connect("C:/barname nevisy/programing/Python/pyth\
                     onProject12/practice/practice8_5databais/d\
                     ata_baiss.db") as connicat:
    connicat.execute(query)
    connicat.commit()

print ("operation was sucessfull!! ")