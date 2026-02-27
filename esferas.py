nivel = int(input("qual seu nivel atual?: "))
esferas = int(input("quantas esferas você tem?: "))

if nivel >= 20 and esferas >= 50:
    print("habilidade super salto desbloqueada.")
elif nivel >= 20 and esferas < 50:
    print("requisitos insuficientes para habilidade.")
elif nivel < 20 and esferas >= 50:
    print("requisitos insuficientes para habilidade")
elif nivel < 20 and esferas < 50:
    print("requisitos insuficientes para habilidade")