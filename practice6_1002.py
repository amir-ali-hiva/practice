from termcolor import colored 
import time
Name = input("Plz Enter You Name: ")

tedad = len(Name)


for i in range(0, tedad + 1 , 1):
    print(colored(f"{Name[0:i]}" , "red"))
    time.sleep(0.5)

print( colored (" ♥" ,"red"), colored( f" {Name} ","blue"), colored("♥", "red"))

