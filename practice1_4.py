min = int (input("Min: "))
max = int(input("Max: "))

if min > max :
    min,max = max,min


while min <= max :
    if min % 2 == 1:#adad fard ra print kone
        print(min)
    min = min +1 
print ("Finish")