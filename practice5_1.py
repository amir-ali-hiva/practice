#comel magsomesh ta miane be she adad
#
n = int(input("Number: "))
conter = 1 
sum = 0


while conter < n :
    if n % conter == 0 :
        sum = sum + conter
    conter += 1


if sum == n:
    print(f"{n} Is Complete.")
else :
    print(f"{n} Is Not Complete.")
