def frete_gratis(valor):
    return valor >= 200

def pode_votar(idade):
 	return idade >= 16

def senha_valida(senha):
 	return len(senha) >= 8

assert frete_gratis(199.99) == False
assert frete_gratis(200) == True
assert frete_gratis(200.01) == True

assert pode_votar(15) == False
assert pode_votar(16) == True
assert pode_votar(17) == True

assert senha_valida("1234567") == False
assert senha_valida("12345678") == True
assert senha_valida("123456789") == True

print("certo")