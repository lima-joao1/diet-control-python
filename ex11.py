leftEdge = int(input("Primeiro número: "))
rightEdge = int(input("Segundo número: "))

totalSum = 0

for i in range(leftEdge, rightEdge + 1): # Considerando intervalo fechado nos dois lados
    print(i, end=" ")
    totalSum += i

print()
print(totalSum)