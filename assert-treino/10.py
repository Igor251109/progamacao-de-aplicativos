#   def classificar_temperatura(temperatura):
 	    # abaixo de 15: "Frio"
 	    # de 15 até 25: "Agradável"
 	    # acima de 25: "Quente"
# 	    pass

def classificar_temperatura(temperatura):
    if temperatura < 15:
        return "frio"
    elif temperatura >= 15 and temperatura <= 25:
        return "agradavel"
    else:
        return "quente"

assert classificar_temperatura(35) == "quente"
assert classificar_temperatura(25) == "agradavel"
assert classificar_temperatura(15) == "agradavel"
assert classificar_temperatura(14) == "frio"
assert classificar_temperatura(26) == "quente"

print("certo.")
