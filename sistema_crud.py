# Objetivo: Construir um sistema de gerenciamento de estoque utilizando Python.
# O sistema deve ser totalmente modularizado, o que significa que cada ação (Criar, Ler, Atualizar, Deletar) deve ser uma função independente.


estoque = []    # local que recebe os nomes dos produtos e ficaram armazenados.

def adicionar_produtos(nome):   # adicionar um novo nome na lista para armazenar.
    estoque.append(nome)
    print(f"produto adicionado! a lista agora é: {estoque}")

def listar_produtos():   # mostrar os produtos que estão na lista.
    len(estoque)
    print(len(estoque))

def atualizar_produto(novo_nome, indice):
    