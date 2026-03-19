while True:
    age = input("Nome: ")
    if (len(age)) > 3:
        print("Nome registrado.")
        break
    print("Nome deve ter mais que três caracteres.")

while True:
    age = int(input("Idade: "))
    if (0 <= age <= 150):
        print("Idade registrada.")
        break
    print("Idade deve estar entre 0 e 150 anos.")

while True:
    salary = int(input("Salário: "))
    if (salary > 0):
        print("Salário registrado.")
        break
    print("Salário deve ser maior do que zero.")

while True:
    gender = input("Gênero (f/m): ")
    if (gender == "f" or gender == "m"):
        print("Gênero registrado.")
        break
    print("Gênero inválido.")

while True:
    maritalStatus = input("Estado civil (s, c, v, d): ")
    validOptions = ["s", "c", "v", "d"]
    if (maritalStatus in validOptions):
        print("Estado civil registrado.")
        break
    print("Estado civil inválido.")
