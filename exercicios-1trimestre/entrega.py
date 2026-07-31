codigo = int(input("qual o codigo do pacote?: "))
peso = int(input("qual o peso do pacote?: "))

if peso < 5 and codigo % 10 == 0:
    print(f"pacote {codigo}: entrega expressa.")

elif peso >= 50:
    print("carga pesada")

else:
    print("entrega normal.")