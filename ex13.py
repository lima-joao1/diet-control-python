base = int(input("Base: "))
exponent = int(input("Expoente: "))
number = 1

for i in range(exponent):
    number *= base

print(number)