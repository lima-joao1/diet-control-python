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
    
    def to_dict(self):

        return {
            "nome" : self.get_name(),
            "gramas" : self.get_grammes(),
            "calorias_porcao" : self.get_caloriesPerPortion(),
            "proteinas" : self.get_proteins(),
            "carboidratos" : self.get_carbo(),
            "gorduras" : self.get_fat()
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["nome"], data["gramas"], data["calorias_porcao"], data["proteinas"], data["carboidratos"], data["gorduras"])