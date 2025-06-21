n = int(input("N: "))

conter = 1 
sum = 0 
text = ""
fact = 1

while conter <= n:
    fact *= conter
    sum += fact
    text += f"({conter}!) + "
    conter += 1
print(f"{text[0:-3]} = {sum}")