senha = "sesi123"
pergunta = input("digite a senha de segurança:")

while pergunta != senha:
    print("senha incorreta! tente novamente.")
    pergunta = input("digite a senha de segurança")
    