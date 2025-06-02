#s = (1/2) + (2/3) + ((n-1)/n)
n = int(input("Number: "))

conter = 1
sum = 0 
text = ""

while n > conter :
    sum = sum + conter / (conter + 1) 
    text = text + f"({conter} / {conter + 1}) + "
    conter = conter + 1
print (f"{text[0:-3]} = {sum}")