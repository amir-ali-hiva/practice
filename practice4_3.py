#چند مد با یک دیگر 

from math import * 

n = int(input("How Many Number: "))

max = -inf
min = inf
sum = 0
conter = 0
number_dictionary = {}

while conter < n :
    a = input (f"Number#{conter + 1}: ")
    if not a.isnumeric() and "-" not in a :
        continue
    number_of_dictionary = number_dictionary.get(f"{a}")
    if number_of_dictionary == None :
        number_dictionary[f"{a}"] = 1
    else :
        number_dictionary[f"{a}"] = number_of_dictionary + 1
    a = int(a)
    if a > max :
        max = a
    if a < min : 
        min = a
    sum = sum + a
    conter = conter + 1
x = number_dictionary.items()
sorted_x = sorted(x, key=lambda vahed: vahed[1])


max_number = sorted_x [-1][1]






print (f"Sum = {sum}")
print (f"Min = {min}")
print (f"Max = {max}")
print (f"Maen = {sum / conter}")#میانگین 
[print(z) for z in sorted_x if z[1] == max_number]