def memoized_fibo(n):
    global fibo
    if fibo [n - 1] != -1 :
        return fibo [n - 1]
    elif n <= 2 :
        fibo[n - 1] = 1
        return fibo[n - 1]
    fibo[n - 1] = memoized_fibo(n - 1) + memoized_fibo(n - 2)
    return fibo[n - 1]



n = int(input("Number: "))
fibo = [-1] * n

result = memoized_fibo(n)
print (result)



