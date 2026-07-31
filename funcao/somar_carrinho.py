lista = [50.0, 67.5, 500.9]
soma= 0
def somar_carrinho(lista, soma):
    for item in lista:
        soma += item

    if soma >= 500:
        desconto = soma * 0.10
        desconto = soma - desconto
        return f"valor com desconto aplicado! o valor atualizado é: {desconto}"
    return soma

carrinho_pronto = somar_carrinho(lista, soma)
print(carrinho_pronto)