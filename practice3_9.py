#s = 1 + 2 + 3 + n
n = int(input("Number: "))

conter = 1
sum = 0 
text = ""

while n >= conter :
    sum = sum + conter
    text = text + f"{conter} + "
    conter = conter + 1 
print (f"{text[0:-3]} = {sum}")