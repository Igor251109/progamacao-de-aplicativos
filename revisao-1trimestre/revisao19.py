valor = float(input("qual o valor total da compra?: "))
desconto = valor * 0.10
desconto_total = valor -desconto

if valor > 100:
    print("o valor com desconto é: ", desconto_total)
else:
    print("desconto indisponivel, o valor total é: ", valor)