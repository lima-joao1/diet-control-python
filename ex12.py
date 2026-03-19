numberTabuada = int(input("Número da tabuada: "))

for i in range(1, 11):
    result =  (numberTabuada * i)
    output = "%d X %d = %d" % (numberTabuada, i, result)
    print(output)