user_correct = "Husky"
password_correct = "001"
tentativas = 3

print("-------- Sistema de Login --------")


while tentativas > 0:
    user = input("Digite o seu Usuario: ")
    password = input("Digite a seu Senha: ")

    if user == user_correct and password == password_correct :
        print("Seu usuario e senha estao corretos")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print("Seu usuario e senha estao incorretos")
            print("Tentativas restantes:", tentativas)
        else:
            print("Seu usuario e senha estao incorretos")
            print("Tentativas esgotadas")
