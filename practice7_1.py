#انواع تابع ها 
Number1 = 100
Number2 = 200
#1
def sum0(a,b):
    return a + b
#2
def sum1 (a, b):
    print(a + b)
#3
def sum2():
    return Number1 + Number2
#4
def sum3():
    print(Number1 + Number2)

number1 = int (input("Number1: "))
number2 = int(input("Number2: "))

result = sum0(number1, number2)
print(result)

result = sum1(number1 , number2)
print(result)

result = sum2()
print(result)

result = sum3()
print(result)