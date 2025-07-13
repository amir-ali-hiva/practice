file = open ("name.txt", "r" , encoding="utf-8")

lines = file.readlines()
file.close()
for line in lines:
    print(line.replace("\n",""))