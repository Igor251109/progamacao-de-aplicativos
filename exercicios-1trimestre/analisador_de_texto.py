def analisar_texto(nome):
    len(nome)
    if len(nome) < 5:
        return "nome de usuario muito curto."
    else:
        return "nome aceito"

print("-" * 40)
nome = input("qual o nome deseja colocar?: ")

print("-" * 40)
texto_analisado = analisar_texto(nome)

print(texto_analisado)
print("-" * 40)