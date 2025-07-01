from math import * 
for i in range(1, 11 , 1):
    for j in range(1, 11 , 1):
        sual = f"{i} * {j}"
        result = eval(sual) #result
        print(f"{j:02d} * {i:02d} = {result:02d}", end="  ")
    print()