#کار با دیکشنری و پیداکردن مد
from math import *

max = -inf
min = inf
sum = 0
conter = 0 
number_dictionary = {}
n = int(input("How Many Number: "))

while conter < n :
    a = input(f"Number#{conter + 1}: ")
    if not a.isnumeric() and "-" not in a :
        continue
    a = int(a)
    number_of_dictionary = number_dictionary.get(f"{a}")
    if number_of_dictionary == None :
        number_dictionary[f"{a}"] =  1
    else :
        number_dictionary[f"{a}"]  = number_of_dictionary + 1
    if a < min :
        min = a
    if a > max : 
        max = a
    sum = sum + a
    conter = conter + 1

x = number_dictionary.items()
sorted_x = sorted(x, key=lambda vahed: vahed[1])




print (f"Sum = {sum}")
print (f"Min = {min}")
print (f"Max = {max}")
print (f"Maen = {sum / conter}")#میانگین 
print (f"Mode = {sorted_x[-1][0]}with {sorted_x[-1][1]} Repetition")
