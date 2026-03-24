from User import User
from UserArchive import UserArchive

from Food import Food
from FoodArchive import FoodArchive

from ConsumptionManager import ConsumptionManager
import json

def save_foods():
    with open("foods.json", "w") as f:
        foods_list = []
        for food in foodArchive.get_foods():
            foods_list.append(food.to_dict())

        json.dump(foods_list, f, indent=2)

def load_foods():
    try:
        with open("foods.json", "r") as f:
            for data in json.load(f):
                foodArchive.add(Food.from_dict(data))
    
    except FileNotFoundError:
        pass

def save_users():
    with open("users.json", "w") as f:
        users_list = []
        for user in userArchive.get_users():
            users_list.append(user.to_dict())
        
        json.dump(users_list, f, indent=2) # sem o indent = 2, cria um dic do lado do outro :((

def load_users():
    try: # precisa do try porque ao abrir o software pela primeira vez, users.json não existe ainda.
        with open("users.json", "r") as f:
            for data in json.load(f):
                userArchive.add(User.from_dict(data)) # from_dict(cls, data) --> User é cls e data é o dict
    except FileNotFoundError:
        pass

def load_dailies():
    try:
        with open("consumption.json", "r") as f:
            return json.load(f)
        
    except FileNotFoundError:
        return []

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
    
    save_foods()
    
def user_register():
    while True:
        print("\n \033[96m     Cadastro de Usuário\n  \033[0m")

        userName = input("Digite o nome a do usuário ser cadastrado: ").strip().capitalize()
        userAge = int(input("Digite a idade: "))
        userWeight = float(input("Digite o peso (kg): "))
        userHeight = float(input("Digite a altura (cm): "))
        userObjective = input("Digite o objectivo (perda/ganho/manter massa): ")

        user = User(userName, userAge, userWeight, userHeight, userObjective)
        userArchive.add(user)

        stopMark = input("\nDeseja adicionar outro usuário? (Y/N): ").strip().lower()

        if (stopMark == "n"):
            break

    save_users()
    
def change_user_data():
    from time import sleep
    user_exists = True
    userArchive.show_users()
    if (not userArchive.get_users()):
        print("Não existem usuários cadastrados.")
        sleep(3)
        return
    print()

    while True:    
        userName = input("Digite o nome do usuário a ter seus dados alterados: ")

        for user in userArchive.get_users():
            if (user.get_name() == userName):
                user_to_be_changed = user
                user_exists = True
                break
            
            user_exists = False

        if (user_exists):
            break

    print("""O que você deseja alterar?
          1 - Idade
          2 - Massa
          3 - Altura
          4 - Objetivo
""")
    
    command = int(input("O que você deseja alterar? [1-4]: "))

    if (command == 1):
        print("Idade atual: %d" % (user_to_be_changed.get_age()) )
        newAge = int(input("Digite a nova idade: "))
        user_to_be_changed.set_age(newAge)
    elif (command == 2):
        print("Massa atual: %f" % (user_to_be_changed.get_weight()))
        newWeight = float(input("Digite o a nova massa: "))
        user_to_be_changed.set_weight(newWeight)
    elif (command == 3):
        print("Altura atual: %f" % (user_to_be_changed.get_weight()))
        newHeight = float(input("Digite a nova altura: "))
        user_to_be_changed.set_height(newHeight)
    elif (command == 4):
        print("Objetivo atual: " + user_to_be_changed.get_objetive())
        newObjective = input("Digite o novo objetivo (ganhar/perder/manter): ")
        user_to_be_changed.set_objetive(newObjective)
    
    save_users()

def command_manager(command):

    if (command == 1):
        user_register()
    elif (command == 2):
        food_register()
    elif (command == 3):
        manager = ConsumptionManager(userArchive.get_users(), foodArchive.get_foods())
        manager.start()
    elif (command == 4):
        print("\n\033[31mUsuários: \033[0m\n")
        userArchive.show_users()
        show_user_history()
    elif (command == 5):
        print("\n\033[31mUsuários: \033[0m\n")
        change_user_data()

def get_command():
    print("*****\033[31mControle de Dieta\033[0m******")
    print("""
1 - Registrar novo usuário
2 - Registrar novo alimento
3 - Adicionar nova entrada para o usuário
4 - Mostrar histórico de usuário
5 - Alterar dados cadastrais de usuário
          
0 - Fechar aplicativo
          """)

    return int(input("Selecione uma opção [0, 5]: "))

def show_user_history():
    from time import sleep

    log = load_dailies()

    userName = input("\nDigite o nome do usuário a ser obtido histórico: ").strip().capitalize()
    
    entries = []
    for entry in log:
        if entry["usuario"] == userName:
            entries.append(entry)
    
    if not entries:
        print(f"Sem registros para {userName}.")
        sleep(5)
        return
    
    for entry in entries:
        print(f"\n{entry['data']} - {entry['usuario']}")
        print(f"Consumo calórico: {entry['calorias']} cal")
        print(f"Consumo proteico: {entry['proteinas']:.2f} g")
        print(f"Consumo de carboidratos: {entry['carboidratos']} g")
        print(f"Consumo de gorduras: {entry['gorduras']} g")
        print(f"Taxa Metabólica Basal: {entry['tmb']} cal")
        print(f"Gasto Energético Total: {entry['get']:.2f} cal\n")
        sleep(2)
    sleep(5)

# Método food_register p/ registrar diferentes tipos de alimentos.
# Método user_register p/ registrar diferentes usuários nos archives.
# Método get_command retorna o comando desejado pelo administrador.
# Método command_manager lida com o comando digitado pelo administrador.

# No momento, software só funciona p/ administrador. (ideia de fazer uma interface p/ usuário checar seu histórico)

# Começo do programa:

userArchive = UserArchive()
foodArchive = FoodArchive()

load_users()
load_foods()
load_dailies()

while True:
    command = get_command()
    if (command == 0):
        print("Fim.")
        break
    command_manager(command)