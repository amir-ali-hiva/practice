#s = (1/2) - (2/3) + ((n-1)/n)
n = int(input("Number: "))

sign = 1
conter = 1
sum = 0 
text = ""

while n > conter :
    char = "+" if sign > 0 else "-"
    sum = sum +  sign * conter / (conter + 1) 
    text = text + f" {char} ({conter} / {conter + 1})"
    conter = conter + 1
    sign = sign * -1
print (f"{text[3:]} = {sum}")