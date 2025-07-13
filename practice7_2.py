#def S(n: int) -> int:
#    if n == 1:
#        return 1
#    else:
#        return S(n - 1) + n
#    
#number = int(input("Number: "))
#result = S(number)
#print(result)

def s(n):
    if n == 1:
        return 1 
    return s(n - 1) + n

a = int (input("Number : "))
result = s(a)
print(result)