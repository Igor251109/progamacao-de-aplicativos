# Crie um progama que peça uma frase ao usuário via INPUT().
# Salve essa frase dentro de um dicionário na chave "mensagem"
# e exporte para um arquivo chamado 'teste.json'.


open('teste.json', 'w').close()

frase = input("escreva uma frase: ")

dados = {
    "mensagem": frase
}

import json

with open('teste.json', 'w') as arquivo:
    json.dump(dados, arquivo)