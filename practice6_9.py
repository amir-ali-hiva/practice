with open ("name.txt" , "r" , encoding = "utf-8") as file:
    lines = file.readlines()
for line in lines:
    print(line.replace("\n" , ""))