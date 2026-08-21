def situacao_faltas(faltas):
    if faltas >= 0 and faltas <= 4:
        return "regular"
    elif faltas >= 5 and faltas <= 10:
        return "atenção"
    else:
        return "reprovado por falta"
    
assert situacao_faltas(0) == "regular"
assert situacao_faltas(4) == "regular"
assert situacao_faltas(5) == "atenção"
assert situacao_faltas(10) == "atenção"
assert situacao_faltas(11) == "reprovado por falta"

print("certo")

#def situacao_faltas(faltas):     como a função estava.
 	# 0 a 4: "Regular"
 	# 5 a 10: "Atenção"
 	# 11 ou mais: "Reprovado por falta"
# 	pass

