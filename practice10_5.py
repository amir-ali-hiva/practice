import sqlite3
from termcolor import colored
import time
import os

def show_menu():
    print("===================================")
    print("please Enter 1 list of students.")
    print("please Enter 2 Search students .")
    print("please Enter 3 Insert students .")
    print("please Enter 4 Update students .")
    print("please Enter 5 Delete students .")
    print("please Enter 6 To exit program .")
    print("====================================")
    give_choice()

def give_choice():
    choice = int(input("Select from the list:"))
    
    match choice:
        case 1 :
            list_stu()
        case 2 :
            search_stu()
        case 3:
            insert_stu()
        case 4:
            Update_students()
        case 5:
            delete_stu()
        case 6:
            exit_c()
        case _:
            print(colored("Not Supported Number.","red"))
    if 1 <= choice <= 6:
        time.sleep(5)
        os.system("cls")
    else:
        time.sleep(3)
        os.system("cls")

def exit_c():
    os.system("cls")
    come_back = int(input("Are you sure to exit program(0:yes 1:no)"))
    if come_back == 1 :
        return
    else:
        for i in range(5 , 0 ,- 1):
            print(colored(f"{i} Seconds to close","red"))
            time.sleep(1)
            os.system("cls")
        exit()

def delete_stu():
    try:
        id = int(input("Id for delete: "))
        query = f"DELETE FROM a WHERE ID = {id};"



        with sqlite3.connect("C:/barname nevisy/programing/Python/pythonProject12/practice/practice8_5databais/data_baiss.db") as connicat:
            connicat.execute(query)
            connicat.commit()

        print (colored(f"operation was sucessfull!! ","green"))

    except:
        print(colored(f"Error was occurred!!","red"))

def Update_students():
    try:
        #n = 0
        #continu_e = ""                               #کد ها برایه ارتقا هستند 
        #while n == 0 :
        id = int(input("ID of the person you want to update: "))
        name = input("Name: ")
        family = input("Family: ")
        Age = int (input("Age: "))
        #continu_e = input("Is the information correct?(yes or no)").lower
   
        #if continu_e == "yes":
        #    n =+ 1
        #else:
        #    n = 0
        query = f"UPDATE a SET 'Name'='{name}', 'Family'='{family}', 'Age' = '{Age}' WHERE Id = {id}; "
        with sqlite3.connect("C:/barname nevisy/programing/Python/pythonProject12/practice/practice8_5databais/data_baiss.db") as connicat:
            connicat.execute(query)
            connicat.commit()
        print(f"{colored('Operation was sucessfull!!','green')}")
    except:
        print(colored(f"Error was occurred!!","red"))

def insert_stu():
    try:
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
        print(f"{colored('Operation was sucessfull!!','green')}")
    except:
        print(colored(f"Error was occurred!!","red"))

def list_stu():
    try:
        query = f"SELECT * FROM stu_list;"

        with sqlite3.connect("C:/barname nevisy/programing/Python/pythonProject12/practice/practice8_5databais/data_baiss.db") as connicat:    
            cursor = connicat.cursor()               
            results = cursor.execute(query)            
        rows = results.fetchall()                  


        for i ,row in enumerate(rows):
            color = "red" if i % 2 == 0  else "yellow"  
            print(colored(f"Name: {row[0]}, Family: {row[1]}, Id: {row[2]}, Age: {row[3]}",color))
    except:
        print(colored(f"Error was occurred!!","red"))   

def search_stu():
    try:
        filter_search = input("[ Name: 0 ,Family: 1 ,Age: 2 ,Id:3 ]: ")
        how_search = input("[ Start with: 0 , End with: 1 , Contains: 2 ,Equals: 3 ]: ")
        query = f"SELECT * FROM a Where "
        match filter_search:
            case "0":
                filter = "Name"
            case "1":
                filter = "family"
            case "2":
                filter = "Age"
            case "3":
                filter = "Id"
            case _:
                print(colored("Not supported","red"))
                return
            
        value = input(f"{filter}: ")
        match how_search :
            case "0":
                query = f"{query} {filter} LIKE '{value}%'"
            case "1":
                query = f"{query} {filter} LIKE '%{value}'"
            case "2":
                query = f"{query} {filter} LIKE '%{value}%'"
            case "3":
                query = f"{query} {filter} LIKE '{value}'"
            case _:
                print(colored("Not supported" , "red"))
                return

        
        
        with sqlite3.connect("C:/barname nevisy/programing/Python/pythonProject12/practice/practice8_5databais/data_baiss.db") as connicat:    
            cursor = connicat.cursor()               
            results = cursor.execute(query)            
        rows = results.fetchall()                  


        for i ,row in enumerate(rows):
            color = "red" if i % 2 == 0  else "yellow"  
            print(colored(f"Name: {row[0]}, Family: {row[1]}, Id: {row[2]}, Age: {row[3]}",color))
    except:
        print(colored(f"Error was occurred!!","red")) 
                 
while True:
    show_menu()