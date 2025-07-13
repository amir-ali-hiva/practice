def prs(n):
    if n == 1 :
        return  "*"
    #return f"{prs (n - 1)}*"
    result = prs(n - 1)
    return f"{result}*"
a = int(input("Number: "))
result = prs(a)
print(result)