#zaman , s = 1 + 2 + 3 + n
import time


n = int(input("Number: "))

conter = 1
sum = 0 
text = ""
start = time.time()
while n >= conter :
    sum = sum + conter
    text = text + f"{conter} + "
    conter = conter + 1 
end = time.time()
print (f"{text[0:-3]} = {sum} zaman = {end - start}")

start = time.time()
sum = n * (n + 1) / 2
end = time.time()
print (f"{text[0:-3]} = {int (sum)} zaman = {end - start}")