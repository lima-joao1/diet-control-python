from User import User
from UserArchive import UserArchive

from Food import Food
from FoodArchive import FoodArchive

from ConsumptionManager import ConsumptionManager
import json


def save_users():
    with open("users.json", "w") as f:
        users_list = []
        for user in userArchive.get_users():
            users_list.append(user.to_dict())
        
        json.dump(users_list, f, indent=2) # sem o indent = 2, cria um dic do lado do outro :((

def load_users():
    with open("users.json", "r") as f:
        for data in json.load(f):
            userArchive.add()
    

def food_register():
    while True:
        print("\n \033[31m     Cadastro de Alimentos\n  \033[0m")

        foodName = input("Digite o nome do alimento: ").capitalize().strip()
        foodGrammes = float(input("Digite a quantidade de gramas de uma porção: "))
        foodCaloriesPerPortion = float(input("Digite a quantidade de calorias por porção: "))
        foodProteins = float(input("Digite a quantidade de proteínas por porção: "))
        foodCarbo = float(input("Digite a quantidade de carboidratos por porção: "))
        foodFat = float(input("Digite a quantidade de gordura por porção: "))

        food = Food(foodName, foodGrammes, foodCaloriesPerPortion, foodProteins, foodCarbo, foodFat)
        foodArchive.add(food)
        
        stopMark = input("\nDeseja adicionar um novo alimento? (Y/N): ").lower()
        print()
    
        if (stopMark == "n"):
            break
    

def user_register():
    while True:
        print("\n \033[96m     Cadastro de Usuário\n  \033[0m")

        userName = input("Digite o nome a do usuário ser cadastrado: ").strip().capitalize()
        userAge = int(input("Digite a idade: "))
        userWeight = float(input("Digite o peso (kg): "))
        userHeight = float(input("Digite a altura (cm): "))
        userObjective = input("Digite o objectivo (perda/ganho/manter massa): ")

        stopMark = input("\nDeseja adicionar outro usuário? (Y/N): ").lower()

        user = User(userName, userAge, userWeight, userHeight, userObjective)
        userArchive.add(user)

        if (stopMark == "n"):
            break 

    save_users()
    
def command_manager(command):
    if (command == 1):
        user_register()
    elif (command == 2):
        food_register()
    elif (command == 3):
        manager = ConsumptionManager(userArchive.get_users(), foodArchive.get_foods())
        manager.start()
def get_command():
    print("***** Controle de Dieta ******")
    print("""
1 - Registrar novo usuário
2 - Registrar novo alimento
3 - Analisar usuário
          
0 - Fechar aplicativo
          """)

    return int(input("Selecione uma opção [0, 5]: "))

# Método food_register p/ registrar diferentes tipos de alimentos.
# Método user_register p/ registrar diferentes usuários nos archives.
# Método get_command retorna o comando desejado pelo administrador.
# Método command_manager lida com o comando digitado pelo administrador.

# No momento, software só funciona p/ administrador. (ideia de fazer uma interface p/ usuário checar seu histórico)



userArchive = UserArchive()
foodArchive = FoodArchive()

while True:
    command = get_command()
    if (command == 0):
        print("Fim.")
        break
    command_manager(command)