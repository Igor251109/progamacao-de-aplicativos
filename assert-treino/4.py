def eh_par(numero):
 	return numero % 2 == 0

assert eh_par(3) == False
assert eh_par(10) == True
assert eh_par(95) == False
assert eh_par(-1280) == True

print("certo.")


#   def eh_par(numero):           assim estava a função
# 	    return numero % 2 == 0

#   assert eh_par(3) is True


resposta = "o erro estava no 'assert'. 3 não é True, pois não é par."
