def pode_votar(idade):
 	return idade >= 16

assert pode_votar(5) == False
assert pode_votar(15) == False
assert pode_votar(16) == True
assert pode_votar(76) == True

print("certo.")