from termcolor import colored
import time
import os

n = int(input("How Many Numbers: "))

conter = 0 
sum = 0 

while conter < n :
    os.system ("cls")
    a = (input(f"Number #{conter + 1}: "))
    if not a.isnumeric() and "-" not in a :          #if not a.lstrip('-').isdigit(): تا
        print(colored("Please Enter Digits","red"))
        time.sleep(0.5)
        continue
    a = int(a)
    conter = conter + 1 
    sum = sum + a
sum = round (sum, 2)
print (f"sum = {sum}")

