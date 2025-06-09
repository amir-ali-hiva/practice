#its traingle or not

a = int(input("Number#1: "))
b = int(input("Number#2: "))
c = int(input("Number#3: "))

if a <= b + c and b <= a + c and c <= a + b :
    print("Is Triangle. ")
else:
    print("Is Not Triangle. ")
    