class ConsumptionManager:

    def __init__(self, users, foods):
        self.__private_users = users
        self.__private_foods = foods
        self.__private_consumedFoods = []
    


    def start(self):
        
        while True:  # Checa se usuário existe. Pede um nome de usuário até este ser válido (ter sido registrado anteriormente)
            print("Usuários: \n")
            for user in self.__private_users:
                print(user.get_name())

            userName = input("\nDigite o nome do usuário em análise: ").strip().capitalize()
            
            if (self.user_exists(userName)):
                break

            else:
                print("Usuário inválido. Tente novamente.")

        while True: # Checa se alimento está nos registros e adiciona a uma lista de consumidos os que estiverem.
            foodName = input("Digite o alimento consumido: ").capitalize()

            if (self.food_exists(foodName)):
                self.add_to_consumed_foods(foodName, self.__private_foods)
                
            
            else:
                print(f"{foodName} não cadastrado. Tente novamente.\n")
                continue

            stopMark = input("Deseja adicionar outro alimento que o usuário consumiu? (Y/N): ").lower()
            
            if (stopMark == "n"):
                break

                
        foodToPortions = self.portion_register() 
        
        user = self.get_user(self.__private_users, userName)
        self.show_details(foodToPortions, user) 


    def show_details(self, foodToPortions, user): # Método que engloba as tarefas de printar todas as informações sobre o usuário em questão.
        
        user_name = user.get_name()
        consumed_calories = 1.0 * self.consumed_calories_total(self.__private_consumedFoods, foodToPortions)
        consumed_proteins = self.consumed_proteins_total(self.__private_consumedFoods,foodToPortions)
        consumed_carbo = self.consumed_carbo_total(self.__private_consumedFoods, foodToPortions)
        consumed_fats = self.consumed_fats_total(self.__private_consumedFoods, foodToPortions)
        tmb = self.basal_metabolic_rate(user.get_age(), user.get_weight())
        activity_factor = self.physical_activity_level()
        get = self.daily_energy_expenditure(tmb, activity_factor)


        print(f"Informações sobre o usuário \033[92m{user_name}\033[0m:\n")

        self.show_foods_portions(foodToPortions, user_name)


        print(f"\nMetabolismo Basal de {user_name}: {tmb:.2f}")
        print(f"Gasto energético total de {user_name}: {get:.2f}")
        print(f"\n{user_name} consumiu um total de {consumed_calories:.2f} calorias.")
        print(f"{user_name} consumiu um total de {consumed_proteins:.2f} g de proteínas.")
        print(f"{user_name} consumiu um total de {consumed_carbo:.2f} g de carboidratos.")
        print(f"{user_name} consumiu um total de {consumed_fats:.2f} g de gorduras.")
        

    
    def portion_register(self): # Método p/ associar cada alimento a uma quantidade consumida num hashmap.
        foodToPortions = {}

        for food in self.__private_consumedFoods:
            portions = int(input(f"Digite quantas porções de {food.get_name()} foram consumidas: "))
            foodToPortions[food] = portions
        
        return foodToPortions
    
    def show_foods_portions(self, foodToPortions, userName): # Método p/ printar tudo que um usuário comeu e quantas porções.
        for key, value in foodToPortions.items():

            if (value == 1):
                print(f"{userName} ingeriu {value} porção de {key.get_name()}.")
            else:    
                print(f"{userName} ingeriu {value} porções de {key.get_name()}.")

    def user_exists(self, userName): # Método p/ checar se o usuário a ser analisado foi registrado anteriormente. (Criar depois método que dá opção de registrar alguém se o nome não existir lá.)

        for user in self.__private_users:
            if (user.get_name() == userName):
                return True
        
        return False
    
    def add_to_consumed_foods(self, foodName, foods): # Método que adiciona um alimento registrado anteriormente à lista de alimento consumidos.
        for food in foods:
            if (food.get_name() == foodName):
                self.__private_consumedFoods.append(food)
                break

    def consumed_fats_total(self, consumed_foods, dictionary_portions):
        fats = 0

        for food in consumed_foods:
            fats += food.get_fat() * dictionary_portions[food]
         
        return fats

    def consumed_carbo_total(self, consumed_foods, dictionary_portions):
        carbo = 0

        for food in consumed_foods:
            carbo += food.get_carbo() * dictionary_portions[food]
        
        return carbo

    def food_exists(self, foodName): # Método que checa se o alimento a ser consultado existe no registro. Análogo a user_exists().


        for food in self.__private_foods:
            if (food.get_name() == foodName):
                return True
        return False
    
    def consumed_calories_total(self, consumedFoods, dictionary_portions):

        calories = 0

        for food in consumedFoods:
            calories += food.get_caloriesPerPortion() * dictionary_portions[food]
        
        return calories
    
    def consumed_proteins_total(self, consumed_foods, dictionary_portions):
        proteins = 0
        for food in consumed_foods:
            proteins += food.get_proteins() * dictionary_portions[food]
        
        return proteins


    def basal_metabolic_rate(self, age, weight): # Método que calcula o Metabolismo Basal de uma pessoa, com base em idade e peso. Dá para melhorar, 
                                                 # pedindo o gênero da pessoa também.

        print("\nA Taxa Metabólica Basal representa quantas calorias o corpo gasta para manter as funções vitais.")

        if (age <= 3):
            return (59.512 * weight) - 30.4
        elif (age <= 10):
            return (22.706 * weight) + 504.3
        elif (age <= 18):
            return (17.686 * weight) + 658.2
        elif (age <= 30):
            return (15.057 * weight) + 692.2
        elif (age <= 60):
            return (11.472 * weight) + 873.1
        elif (age >= 60):
            return (11.711 * weight) + 587.7

    def daily_energy_expenditure(self, tmb, fa):

        print("\nO gasto energético total representa a quantidade de calorias média gasta pelo corpo diariamente.")
        
        return tmb * fa

    def physical_activity_level(self):
        
        print("""\nNível de atividade física do usuário\n:
1 - Sedentário: trabalho de escritório, pouco movimento.
2 - Leve: exercício leve 1-3 dias por semana.
3 - Moderado: exercício moderado 3-5 dias por semana.
4 - Intenso: exercício pesado 6-7 dias por semana.
5 - Atleta: treino pesado diário ou trabalho físico braçal.""")
        
        physical_activity = int(input("Digite um valor no intervalo [1-5]: "))

        if (physical_activity == 1):
            return 1.2
        elif (physical_activity == 2):
            return 1.375
        elif (physical_activity == 3):
            return 1.55
        elif (physical_activity == 4):
            return 1.725
        elif (physical_activity == 5):
            return 1.9
            
    def get_user(self, users, userName):
        for user in users:
            if (user.get_name() == userName):
                return user