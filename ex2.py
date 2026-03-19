while (True):
    username = input("Nome de usuário: ")
    password = input("Senha: ")

    if username != password:
        break

    print("O nome de usuário deve ser diferente da senha.")

print("Usuário registrado.")