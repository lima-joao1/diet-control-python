class UserArchive:

    def __init__(self):
        self.__private_users = []
    
    def add(self, user):
        self.__private_users.append(user)
    
    def get_users(self):
        return self.__private_users
    
    def show_users(self):
        for user in self.__private_users:
            print(user.get_name())