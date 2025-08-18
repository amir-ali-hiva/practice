from termcolor import colored
#sercch
try:
    filter_search = int(input("[ Name: 0 ,Family: 1 ,Age: 2 ,Id:3 ]: "))
    how_search = int(input("[ Start with: 0 , End with: 1 , Contains: 2 ,Equals: 3 ]: "))
    
    match filter_search:
        case 0:
            filter = "Name"
        case 1:
            filter = "family"
        case 2:
            filter = "Age"
        case 3:
            filter = "Id"
        case _:
            print(colored("Not supported","red"))
           
        

except:
    print()