
n  = int(input("Number: "))
sum = 0
text = ""
conter = 1

while conter <= n :
    sum = sum + conter
    text = text + f"{conter} + "
    conter = conter + 1
print(f"{text[0:-3]} = {sum}")
