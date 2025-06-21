min = int(input("Min: "))
max = int(input("Max: "))

if min > max:
    min, max = max, min

while min <= max :
    n = min

    sum = 0
    conter = 1 

    while conter < n :
        if n % conter == 0:
            sum += conter
        conter += 1


    if sum == n :
        print(f"{n} Is complete. ")
    min += 1 
    