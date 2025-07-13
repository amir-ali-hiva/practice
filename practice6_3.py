row = int(input("Row: "))

col = row * 2  - 1          #تاثیر -1 در این فرمول؟

mid = col // 2
conter = 0


for i in range (0, row , 1):
    for j in range (0, col , 1):
        if  mid - conter <= j <= mid + conter :
            print("*", end="")
        else :
            print("-", end="")
    print()
    conter += 1