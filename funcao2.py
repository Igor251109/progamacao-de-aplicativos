def validadar_senha(senha):
    while len(senha):
        if senha < 6:
            False
            return "erro."
        elif senha >= 6:
            True
            return "senha cadastrada com sucesso."

senha = input("digite sua senha: ")
senha_final = validadar_senha(senha)
print(senha_final)