salary = float (input("salary : "))

insurance = salary * 5 / 100
home = salary * 10 /100

sum = home + insurance

puresalary = salary - sum

print(f"insurance: {insurance}")
print(f"Home: {home}")
print(f"sum: {sum}")
print (f"puresalary: {puresalary}")
