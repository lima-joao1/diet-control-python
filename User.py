class User:

    def __init__(self, name, age, weight, height, objective):
        self.__private_name = name
        self.__private_age = age
        self.__private_weight = weight
        self.__private_height = height
        self.__private_objective = objective
    
    def get_name(self):
        return self.__private_name
    
    def set_name(self, name):
        self.__private_name = name

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
        self.__private_objective = objective
    
    def to_dict(self):

        return {
            "nome": self.get_name(),
            "idade": self.get_age(),
            "peso": self.get_weight(),
            "altura": self.get_height(),
            "objetivo": self.get_objective()
        }

    @classmethod    # Decorator que faz o método abaixo receber a classe como argumento.
    def from_dict(cls, data): # cls = class, data é um dictionary que como argumento será passado
        return cls(data["nome"], data["idade"], data["peso"], data["altura"], data["objetivo"])
        # cls(...) usará o construtor da classe passada como parâmetro p/ criar objetos dela, tipo
        # quando faz user = User(userName, userAge, userWeight, userHeight, userObjective), só que 
        # é feito sem vc escrever. Retorna o objeto da classe dada como parâmetro