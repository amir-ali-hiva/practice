#s = (1/3) + (2/9) + ((n)/3**n)
n = int(input("Number: "))

conter = 1
p = 3 
sum = 0 
text = ""

while n >= conter :
    sum = sum + conter / (p) 
    text = text + f"({conter} / {p}) + "
    conter = conter + 1
    p = p * 3
print (f"{text[0:-3]} = {sum}")