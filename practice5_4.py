min = int(input("Min: "))
max = int(input("Max: "))

if min > max :
    min , max = max , min 

while min <= max :
    n = min 
    conter = 1
    sum = 0 
    num = 0

    text = ""
    while conter <= n:
        if n % conter == 0:
            
            sum +=conter
            num +=1 
            text = text + f"{conter} , "
        conter += 1
    min += 1
    print (f"{n}: ( {text[0:-2]}), Sum: {sum}, Num = {num} ")