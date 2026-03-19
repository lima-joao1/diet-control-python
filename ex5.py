while True:
    populationA = int(input("População de A: "))
    if (populationA > 0):
        break
    print("População da cidade A é inválida.")

while True:
    anualGrowthA = float(input("Crescimento anual de A: ")) # 3% => 0.03 => 1.03
    if (anualGrowthA > 1):
        anualGrowthA = (anualGrowthA / 100) + 1
        break
    print("Taxa de crescimento de A inválida.")

while True:
    populationB = int(input("População de B: "))
    if (populationB > 0):
        break
    print("População de B é inválida.")

while True:
    anualGrowthB = float(input("Crescimento anual de B: "))
    if (anualGrowthB > 1):
        anualGrowthB = (anualGrowthB / 100) + 1
        break
    print("Taxa de cescimento de B é inválida.")

yearsNeeded = 0

while (populationA < populationB):
    yearsNeeded += 1

    populationA *= anualGrowthA
    populationB *= anualGrowthB

print("Anos necessários: %d." % (yearsNeeded))