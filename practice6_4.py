row = int(input("Row: "))

col = row 

mid = col // 2
conter = 0


for i in range (0, row , 1):
    for j in range (0, col , 1):
        if  mid - conter <= j <= mid + conter :
            print("*", end="")
        else :
            print(" ", end="")
    print()
    if i >= mid:
        conter -= 1
    else:
        conter += 1