media = float(input("qual a sua média final?: "))
presenca = int(input("qual sua porcentagem de presença?: "))

if media >= 7.0 and presenca >= 75:
    print("aprovado")
elif media < 7.0 and presenca < 75:
    print("reprovado")
elif media < 7.0 and presenca >= 75:
    print("reprovado")
elif media >= 7.0 and presenca < 75:
    print("reprovado")