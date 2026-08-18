def situacao_aluno(media):

    if media >= 6:

        return "Aprovado"

    elif media >= 4:

        return "Recuperação"

    return "Reprovado"

assert situacao_aluno(7) == "Aprovado"
assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(4) == "Recuperação"
assert situacao_aluno(4.1) == "Recuperação"
assert situacao_aluno(3.7) == "Reprovado"

print("tudo certo.")