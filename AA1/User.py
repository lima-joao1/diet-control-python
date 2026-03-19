class User:

    def __init__(self, name, age, weight, height, objective):
        self.__private_name = name
        self.__private_age = age
        self.__private_weight = weight
        self.__private_height = height
        self.__private_objective = objective
    
    def get_name(self):
        return self.__private_name
    
    def get_age(self):
        return self.__private_age

    def set_age(self, age):
        self.__private_age = age

    def get_weight(self):
        return self.__private_weight
    
    def set_weight(self, weight):
        self.__private_weight = weight
    
    def get_height(self):
        return self.__private_height

    def set_height(self, height):
        self.__private_height = height

    def get_objective(self):
        return self.__private_objective
    
    def set_objective(self, objective):
        self.__private_ojective = objective