nome = input("digite seu nome: ")
altura = float(input("digite sua altura: "))

if altura >= 1.50:
    print("acesso liberado! dirvirta-se", nome)
if altura < 1.50:
    print("desculpa, você não tem a altura minima", nome)