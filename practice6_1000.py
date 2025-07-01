

col = int(input("Col: "))
row = int (input("Row: "))


for i in range (0, row , 1):
    for j in range(0, col , 1):
        if i == 0 or i == row - 1 :
            print("*", end="")
        else:
            if i + j == i or i + j == i + col - 1:
                print("*", end="")
            else:
                print(" ", end="")
    print()