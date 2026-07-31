valor = float(input("digite o valor da compra: "))
cupom = input("qual o cupom?: ")
nome_do_cupom = "dev10"

desconto = valor * 0.10
novo_valor = valor - desconto

if nome_do_cupom == "dev10":
    print("cupom valido: ", novo_valor)
else:
    print("cupom invalido: ", valor)
