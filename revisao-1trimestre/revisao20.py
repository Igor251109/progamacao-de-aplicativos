pedidos = input("qual produto quer comprar?: ")
lista =[]

while pedidos != "sair":
    print("produto adicionado na lista")
    pedidos = input("qual proximo produto?: ")
    print("-" * 60)
    if pedidos == "sair":
        print("lista concluida! o resultado é: ", lista)
        break
    lista.append(pedidos)
    
print("-" * 60)