min = int(input ("Min: "))
max = int (input("MAx: "))

answer = input ("Odd or Ever :").lower()

if answer in ["odd"]:#fard
    R = 1
else :#zog
    R = 0

if min > max :
    min,max = max,min

while min <= max :
    if min % 2 == R :
        print (min)
    min = min + 1
print("Finish")