def eh_par(numero):
    if numero % 2 == 0:
        return "o número é par."
    return "o número é impar."


def calcular_desconto(preco, percentual):
    media = preco - percentual
    return media
    # Retorne o valor final após aplicar o desconto
    


def pode_votar(idade):
    if idade < 16:
        return "não pode votar."
    elif idade >= 16 and idade < 18:
        return "voto facultativo."
    else:
        return "voto obrigatório"

assert eh_par(6) == "o número é par."
assert eh_par(17) == "o número é impar."

assert calcular_desconto(100, 0.10)
assert calcular_desconto(590, 0.90)
assert calcular_desconto(100, 0.35)

assert pode_votar(15) == "não pode votar."
assert pode_votar(17) == "voto facultativo."
assert pode_votar(22) == "voto obrigatório"

print("todos passaram")