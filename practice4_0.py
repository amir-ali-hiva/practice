#hesab max va min
from math import * 

n = int(input("How Many Number: "))

conter = 0
sum = 0 
max = -inf
min = inf


while conter < n :
    a = input(f"numer #{conter + 1}:")
    if not a.isnumeric() and "-" not in a :
        continue
    a = int(a)
    if a > max :
        max = a 
    if a < min : 
        min = a
    conter = conter + 1
    sum = sum + a
print (f"Sum = {sum}")
print (f"Min = {min}")
print (f"Max = {max}")