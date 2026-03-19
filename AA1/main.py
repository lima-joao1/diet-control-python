from User import User
from UserArchive import UserArchive

userArchive = UserArchive()

while True:
    print("\033[96m     Cadastro de usuário\n  \033[0m")

    userName = input("Digite o nome: ")
    userAge = int(input("Digite a idade: "))
    userWeight = float(input("Digite o peso: "))
    userHeight = float(input("Digite a altura: "))
    userObjective = input("Digite o objective (perda/ganho/manter massa): ")

    stopMark = input("Deseja adicionar outro usuário? (Y/N): ").lower()

    user = User(userName, userAge, userWeight, userHeight, userObjective)
    userArchive.add(user)

    if (stopMark == "n"):
        break


while True:
    print("\033[31m     Cadastro de alimentos\n  \033[0m")

    foodName = input("Digite o nome do alimento:")
    
    
print(user.get_name())
userArchive.show_users()