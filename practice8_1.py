def fibo(n):
    if n <= 2:
        return 1 
    return fibo(n - 2) + fibo(n - 1)

a = int(input("Number: "))

result = fibo(a)
print (result)