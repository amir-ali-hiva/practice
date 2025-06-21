from termcolor import colored
import os
n = int(input("Number: "))

num = 0 
conter = 1 

while conter <= n :
    os.system("cls")
    if n % conter == 0:
        num += 1
    conter += 1

if num == 2 :
    print(colored(f"{n} Is Prime","green"))

else :
    print(colored(f"{n} Is Not Prime ","red"))
