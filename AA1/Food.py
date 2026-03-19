class Food:

    def __init__(self, name, grammes, caloriesPerPortion, proteins, carbo, fat):
        self.__private_name = name
        self.__private_grammes = grammes
        self.__private_caloriesPerPortion = caloriesPerPortion
        self.__private_proteins = proteins
        self.__private_carbo = carbo
        self.__private_fat = fat
    
    def get_name(self):
        return self.__private_name

    def get_grammes(self):
        return self.__private_grammes

    def get_caloriesPerPortion(self):
        return self.__private_caloriesPerPortion
    
    def get_proteins(self):
        return self.__private_proteins

    def get_carbo(self):
        return self.__private_carbo

    def get_fat(self):
        return self.__private_fat