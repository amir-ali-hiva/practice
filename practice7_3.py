
#فاکتور یل به صورت تابع بازگشتی 
def fact (n):
    if n == 1:
        return 1
    return fact(n - 1) * n
 
a = int (input("number: "))
result = fact (a)
print(result)