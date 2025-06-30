row = int(input("Row: "))

for i in range(0, row , 1):
    for j in range(0, row , 1):
        if j >= row - 1 - i :
            print("*", end="")
        else :
            print(" ", end="")
    print()