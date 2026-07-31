senha_correta = "python123"
senha = input("qual a senha correta?: ")

while senha != senha_correta:
    print("senha incorreta.")
    senha = input("digite novamente: ")
else:
    print("senha correta.")