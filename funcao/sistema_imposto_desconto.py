def calcular_valor(valor_base, imposto_percentual, cupom_desconto):   # Uma loja precisa calcular o preço final de um produto considerando o imposto estadual e um cupom de desconto.
    valor = valor_base - imposto_percentual
    valor_com_cupom = valor - cupom_desconto
    if cupom_desconto > valor:
        valor = 0
        return f"o valor total do produto com impostos e descontos é: {valor}."
    elif cupom_desconto < valor:
        return f"o valor total do produto com impostos e descontos é: {valor_com_cupom}."

print("-" * 45)
v1 = float(input("qual o valor do produto?: "))

print("-" * 45)
v2 = float(input("qual o valor do imposto?: "))

print("-" * 45)
v3 = float(input("qual o valor do cupom de desconto?: "))

print("-" * 45)
valor_total_produto = calcular_valor(v1, v2, v3)
print(valor_total_produto)

print("-" * 45)