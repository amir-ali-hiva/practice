min = int (input("Min: "))
max = int (input("Max: "))

while min > max :
    print("Max va Min ra be dorosty vared konid :/")
    min = int (input("Min: "))
    max = int (input("Max: "))

sum = 0
text = ""
while max >= min :
    sum = min + sum
    text = text + f"{min} + "
    min = min + 2

print (f"{text[0:-3]} = {sum}")