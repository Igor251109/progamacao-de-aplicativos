altura = float(input("qual a sua altura?: "))
peso = float(input("qual o seu peso atual?: "))

if peso / altura >= 25:
    print("atenção! você está com sobrepeso.")
else:
    print("peso dentro do recomendado.")