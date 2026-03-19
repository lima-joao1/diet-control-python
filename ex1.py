grade = int(input("Nota: "))

while not(0 <= grade <= 10):
    print("Valor inválido")
    grade = int(input("Nota: "))

print(grade)