row = int(input("Row: "))
col = int(input("Column: "))

for j in range(1 , row + 1 , 1):
    for i in range(1 , col + 1 , 1):
        print("*",end="")
    print()