names = ["Amir_Ali","Ali","Amir","Ali_raza","MJ"]

#conter = 1
#while len(names) > conter :
#    print(f"♥{names[conter]}♥")
#    conter += 1

#for i in range (0, len(names) , 1):
#    print(f"♥{names[i]}♥")

#for name in names:
#    print(f"♥{name}♥")


#new_names = list(map(lambda x:f"♥{x}♥", names))
def g(x):
    return f"♥{x}♥"
new_names = list(map(g , names))


[print(x) for x in new_names]