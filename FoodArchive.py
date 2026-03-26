class FoodArchive:
    
    def __init__(self):
        self.__private_foods = []

    def get_foods(self):
        return self.__private_foods
    
    def add(self, food):
        self.__private_foods.append(food)
        
    def show_foods(self):
        for food in self.__private_foods:
            print(food.get_name())