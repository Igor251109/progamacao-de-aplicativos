# Sistema de Matrícula com ID Manual
# Contexto: A secretaria de uma escola quer gerenciar o cadastro de seus alunos através de um sistema de fichas numeradas.
#  Cada aluno deve receber um Número de Identificação (ID) que a própria secretaria vai escolher e digitar no momento do cadastro.
#Desenvolver um CRUD completo (Criar, Ler, Atualizar e Deletar) em Python, utilizando um arquivo chamado alunos.json para armazenar uma lista de dicionários.

import json
import os

dados_alunos = 'alunos.json'


def cadastrar_aluno():
    print('==== Cadastrar Aluno ====\n')
    
    dados = {
        "id": int(input("qual ID desejado?: ")),
        "nome": input("qual o nome completo do aluno?: "),
        "cpf": int(input("qual o CPF?: ")),
        "telefone": int(input("qual o telefone do aluno?: ")),
        "idade": int(input("qual a idade do aluno?: ")),
        "turma": int(input("qual a turma do aluno?: "))
    }

    if os.path.exists(dados_alunos):
        with open("alunos.json", 'r') as arquivo:
            json.load(arquivo)
    
    else:
        lista = []

    lista.append(dados)

    if dados["id"]:
        print("operação cancelada!o ID já existe.")

    with open(dados_alunos, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    
    print("aluno adicionado com sucesso!")


def listar_aluno():
    print('==== lISTAR ALUNOS ====\n')
    if os.path.exists(dados_alunos):
        with open(dados_alunos, 'r', encoding='utf-8') as arquivo:
            alunos = arquivo.load()
    
    else:
        alunos = []

    if not alunos:
        print('a lista está vazia.')
        return

    


    

def atualizar_aluno():
    listar_aluno()

    idx = int(input('qual o ID do aluno que deseja atualizar?: '))

