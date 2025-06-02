from math import * 

operator = input("Sin,Cos,Tan,Sqrt :").lower()


if operator in ["sin","cos","tan","sqrt"] :

    number = int(input("Number :"))
    if operator in ["sin","cos","tan"]:
         x = number * pi /180
         equatoin = f"{operator}({x})"
    else:
        equatoin =f"{operator} ({number})"

    result = eval (equatoin)
    print (f"{operator}({number}) = {result}")



else:
     number1 = int(input("Number1 :"))
     number2 = int(input("Number2 :"))
     equatoin = f"{number1} {operator} {number2}"
     result = eval (equatoin)
     print(f"{equatoin} = {result}")
     