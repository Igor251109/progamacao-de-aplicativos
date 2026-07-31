nome = input("qual seu nome?: ")
valor = float(input("qual valor total?: "))
distancia = int(input("qual a distância?: "))
cupom = input("cupom especial?: ")

desconto_vip = valor / 0.20
desconto = valor / 0.10
frete = 40
valor_total = desconto_vip - valor

if valor >= 1.000 and cupom == "s" and desconto_vip:
    print("desconto de 20 porcento aplicado")
elif valor > 500 < 1.000 and cupom == "s" and desconto:
    print("desconto de 10 porcento aplicado")
elif distancia <= 50 and frete == 0 and valor >= 200 and desconto:
    print("frete gratis")
elif distancia > 50 and frete:
    print("frete de 40 ")
elif nome and desconto_vip:
    print("parabens! você ganhou um mouse pad gamer de brinde!")

print("nome: ", nome)
print("o valor original é: ", valor)
print("desconto 10%: ", desconto)
print("desconto 20%: ", desconto_vip)
print(valor_total)