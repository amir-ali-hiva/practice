row = int(input("Row: "))

for i in range(0, row , 1):
    for j in range(0, i + 1 , 1):
        print("*", end="")
    print()