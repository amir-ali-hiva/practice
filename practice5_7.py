n = int(input("Number: "))

fact = 1
text = ""


for conter in range (1, n + 1, 1):
    text += f"{conter} * "
    fact *= conter
print(f"{n}! = {text[0:-3]} = {fact}")

