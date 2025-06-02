#s = (1/1) + (1/2) + (1/n)
n = int(input("Number: "))

conter = 1
sum = 0 
text = ""

while n >= conter :
    sum = sum + 1 / conter 
    text = text + f"(1 / {conter}) + "
    conter = conter + 1 
print (f"{text[0:-3]} = {sum}")