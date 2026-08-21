def calcular_desconto(preco, percentual):
 	return preco - (preco * percentual / 100)

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(250, 10) == 225
assert calcular_desconto(100, 25) == 75

print("certo")


#    def calcular_desconto(preco, percentual):     assim estava a função.
#       	return preco - percentual