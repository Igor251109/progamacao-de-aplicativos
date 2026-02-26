idade = int(input("qual a sua idade?: "))
saldo = float(input("qual seu saldo atual?: "))

if idade >= 18 and saldo >= 50:
    print("Acesso autorizado! Bem vindo ao evento.")
elif idade < 18 and saldo < 50:
    print("infelizmente você não cumpre os requisitos de entrada.")