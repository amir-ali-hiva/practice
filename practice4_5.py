#اف داخل هم 
#مثل هست یا نه
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a <= b + c:
    if b <= a + c:
        if c <= a + b:
            print("Is Triangle. ")
        else:
            print("Is Not Triangle. ")
    else:
        print("Is Not Triangle. ")
else:
    print("Is Not Triangle. ")
