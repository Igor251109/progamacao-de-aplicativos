def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def verificar_situacao(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"


# Testes da função calcular_media
assert calcular_media(8, 6) == 7
assert calcular_media(10, 10) == 10
assert calcular_media(0, 0) == 0

# Testes da função verificar_situacao
assert verificar_situacao(7) == "Aprovado"
assert verificar_situacao(6) == "Aprovado"
assert verificar_situacao(5.9) == "Reprovado"

print("Todos os testes passaram!")