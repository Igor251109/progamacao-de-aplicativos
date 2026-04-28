def analisar_texto(quantidade):
    len(quantidade)
    if quantidade < 5:
        return "nome de usuario muito curto."
    else:
        return "nome aceito"

nome = input("qual o nome deseja colocar?: ")
len(nome)
texto_analisado = analisar_texto(nome)
print(texto_analisado)