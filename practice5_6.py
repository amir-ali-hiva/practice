n = int(input("Number: "))

conter = 1 
fact = 1 
text = ""

while n >= conter:
    fact *= conter
    text += f"{conter} * "
    conter += 1


print(f"{n}! = {text[0:-3]} = {fact}")