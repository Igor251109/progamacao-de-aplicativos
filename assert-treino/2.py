def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"

assert situacao_aluno(8) == "Aprovado"
assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(10) == "Aprovado"
assert situacao_aluno(5.9) == "Reprovado"
assert situacao_aluno(0) == "Reprovado"
assert situacao_aluno(6.1) == "Aprovado"   # acho importante

print("certo")

 # Crie testes para as médias: 6, 5.9, 0 e 10.

 # 6 e 5.9 são os casos de limite pois 6 é o ultima numero antes de ser "reprovado" e 5.9 é o ultimo anres de ser "aprovado".