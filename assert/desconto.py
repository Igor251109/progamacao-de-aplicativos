def calcular_desconto(preco, percentual):

    return preco - (preco * percentual / 100)

assert calcular_desconto(100, 0) == 100
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(100, 50) == 50
assert calcular_desconto(100, 100) == 0
assert calcular_desconto(100, 20.5) == 79.5

print("tudo certo.")