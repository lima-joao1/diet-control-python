numbers = []

for i in range(10):
    number = int(input("Número: "))
    numbers.append(number)

amountEven = amountOdd = 0

for num in numbers:
    if (num % 2 == 0):
        amountEven += 1
    else:
        amountOdd += 1

print("Quantidade de números pares: %d." % (amountEven))
print("Quantidade de números ímpares: %d." % (amountOdd))