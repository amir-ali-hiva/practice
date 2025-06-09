#توابع اماده
import scipy.stats as sp
import numpy as np


n = int(input("How Many Number: "))

conter = 0 
number_list = []
while conter < n :
    a = input(f"Number #{conter + 1}: ")
    if not a.isnumeric() and "-" not in a:
        continue
    a = int(a)

    number_list.append(a)

    conter = conter + 1


sum = np.sum(number_list)
mean = np.mean(number_list)
std = np.std(number_list)
max = np.max(number_list)
min = np.min(number_list)
mode = sp.mode(number_list)
median = np.median(number_list)

print(f"Sum = {sum}")
print(f"Mean = {mean}")
print(f"Std = {std}")
print(f"Median = {median}")
print(f"Max = {max}")
print(f"Min = {min}")
print(f"Mode = {mode}")

