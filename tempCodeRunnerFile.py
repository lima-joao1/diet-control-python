from User import User
from UserArchive import UserArchive

from Food import Food
from FoodArchive import FoodArchive

from ConsumptionManager import ConsumptionManager

userArchive = UserArchive()
foodArchive = FoodArchive()

def user_register():
    while True:
        print("\033[96m     Cadastro de usuário\n  \033[0m")

        userName = input("Digite o nome a do usuário ser cadastrado: ")
        userAge = int(input("Digite a idade: "))
        userWeight = float(input("Digite o peso: "))
        userHeight = float(input("Digite a altura: "))
        userObjective = input("Digite o objectivo (perda/ganho/manter massa): ")

        stopMark = input("Deseja adicionar outro usuário? (Y/N): ").lower()

        user = User(userName, userAge, userWeight, userHeight, userObjective)
        userArchive.add(user)

        if (stopMark == "n"):
            break
        
def food_register():
    while True:
        print("\033[31m     Cadastro de alimentos\n  \033[0m")

        foodName = input("Digite o nome do alimento: ")
        foodGrammes = float(input("Digite a quantidade de gramas de uma porção: "))
        foodCaloriesPerPortion = int(input("Digite a quantidade de calorias por porção: "))
        foodProteins = float(input("Digite a quantidade de proteínas por porção: "))
        foodCarbo = float(input("Digite a quantidade de carboidratos por porção: "))
        foodFat = float(input("Digite a quantidade de gordura por porção: "))

        food = Food(foodName, foodGrammes, foodCaloriesPerPortion, foodProteins, foodCarbo, foodFat)
        foodArchive.add(food)

        stopMark = input("Deseja adicionar um novo alimento? (Y/N): ").lower()
        print()
        if (stopMark == "n"):
            break

# Cadastro de Usuários

user_register()

# Cadastro de alimentos

food_register()

# Consumo diário

manager = ConsumptionManager(userArchive.get_users(), foodArchive.get_foods())
manager.start()