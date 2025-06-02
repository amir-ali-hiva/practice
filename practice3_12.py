#s = (1/2) + (1/4) + (1/n)
n = int(input("Number: "))

conter = 2
sum = 0 
text = ""

while n >= conter :
    sum = sum + 1 / conter 
    text = text + f"(1 / {conter}) + "
    conter = conter + 2
print (f"{text[0:-3]} = {sum}")