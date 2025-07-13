def prs(n):
    if n == 1 :
        print("*", end="")
    else:
        print("*", end="")
        prs(n - 1)
    
number = int (input("Number: "))
prs(number)