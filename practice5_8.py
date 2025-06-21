n = int(input("N: "))

text = ""
fact = 1 
sum = 0

for conter in range(1, n + 1, 1):
    fact *= conter
    sum += fact
    text += f"{conter}! + "    
print(f"{text[0:-3]} = {sum}")