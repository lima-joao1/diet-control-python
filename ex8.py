numbers = []

for i in range(5):
    number = int(input("Número: "))
    numbers.append(number)

totalSum = sum(numbers)
averageNumbers = totalSum / len(numbers)

print("Soma: %d" % (totalSum))
print("Média: %d" % (averageNumbers))