import time
import os
from math import *

max = -inf
min = inf
n = 0
b = 0
conter = 0

while n == b:
    os.system("cls")
    a = input (f"number #{conter + 1}: ")
    if not a.isnumeric() and "-" not in a :
        continue
    a = int(a)
    if max <= a:
        os.system("cls")
        max = a
    if min >= a:
        os.system("cls")
        min = a
    print(f"MAx = {max}")
    print(f"Min = {min}")
    conter = conter + 1
    time.sleep (1)
    if conter % 2 == 0 :
        anser = input("Do you want continue(Yes or No): ").lower()
        if anser in ["yes"]:
            b = 0
        else :
            b = 1

print(f"MAx = {max}")
print(f"Min = {min}")

print("Finish")