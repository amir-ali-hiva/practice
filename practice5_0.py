n = int(input("Number: "))

conter = 1 
sum = 0 
num = 0
text = "" 


while conter <= n:
    if n % conter == 0:
        text = text + f"{conter} , "
        sum = sum + conter
        num = num + 1
    conter += 1
print(f"({text[0:-2]}) , Sum = {sum} , Num = {num} ")