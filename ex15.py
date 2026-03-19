firstNumber = 0
secondNumber = 1

n = int(input("N-ésimo termo: "))

output = ""
for i in range(n - 2):
    nextNumber = firstNumber + secondNumber
    output += "%d %d %d" % (firstNumber, secondNumber, nextNumber) 

    firstNumber = secondNumber
    secondNumber = nextNumber

print(output)