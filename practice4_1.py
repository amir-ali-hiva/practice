#ساخت دیکشنری 
from math import * 

n = int(input("How  Many Number: "))

max = -inf
min = inf
sum = 0 
conter = 0 
number_dictionary = {}

while conter < n :
    a = input(f"Number#{conter + 1}: ")
    if not a.isnumeric() and "-" not in a :                  #اگر عدد نبود و "-"هم نداشت
        continue
    a = int(a)
    number_of_dictionary = number_dictionary.get(f"{a}")
    if number_of_dictionary == None :
        number_dictionary[f"{a}"] = 1
    else :
        number_dictionary[f"{a}"] = number_of_dictionary + 1
    if a > max :
        max = a
    if a < min :
        min = a
    conter = conter + 1
    sum = sum + a

print (f"Sum = {sum}")
print (f"Min = {min}")
print (f"Max = {max}")
print (f"Maen = {sum / conter}")#میانگین 
print (f"Number_dictionary = {number_dictionary}")
