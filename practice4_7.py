#Adad ke dar tagsim bigy mande nadaran
n = int(input("Numer: "))

conter = 1
text = ""

while n >= conter:
    if n % conter == 0 :
        text = text + f"{conter} , "
    conter = conter + 1
print(f"{n} : ({text[0:-2]})")