from termcolor import colored
import time
import os

t = int(input("Time: "))

while t >= 0:
    os.system("cls")
    hour = t // 3600
    minet =(t % 3600) // 60
    secent = t % 60
    if t >= 10 :    
        print (f"{hour:02d}:{minet:02d}:{secent:02d}")
    else :
        print (colored (f"{hour:02d}:{minet:02d}:{secent:02d}","red"))
    t = t-1
    time.sleep(1)