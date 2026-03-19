populationA = 80000
anualGrowthA = 1.03
populationB = 200000
anualGrowthB = 1.015
yearsNeeded = 0

while (populationA < populationB):
    yearsNeeded += 1

    populationA *= anualGrowthA
    populationB *= anualGrowthB

print("Anos necessários: %d." % (yearsNeeded))