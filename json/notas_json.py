# Crie manualmente um arquivo chamado "notas.json" com o seguinte conteúdo:
# {"matematica" : 8.5, "portugues" : 9.0}.
# Agora, crie um script python que leia esse arquivo e mostre na tela a soma das duas notas.

open('notas.json', 'w').close()

import json

notas = {
    "matematica" : 8.5,
    "portugues" : 9.0,
    "soma" : 0
    }


dados_completos = notas['matematica'] + notas['portugues']
notas['soma'] = dados_completos

with open('notas.json', 'w') as arquivo:
    json.dump(notas, arquivo)