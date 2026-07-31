# Sistema de Matrícula com ID Manual
# Contexto: A secretaria de uma escola quer gerenciar o cadastro de seus alunos através de um sistema de fichas numeradas.
#  Cada aluno deve receber um Número de Identificação (ID) que a própria secretaria vai escolher e digitar no momento do cadastro.
#Desenvolver um CRUD completo (Criar, Ler, Atualizar e Deletar) em Python, utilizando um arquivo chamado alunos.json para armazenar uma lista de dicionários.

import json
import os

dados_alunos = 'alunos.json'


def cadastrar():
    print("\n--- Novo Cadastro ---")
    
    if os.path.exists(dados_alunos):
        with open(dados_alunos, 'r', encoding='utf-8') as f:
            alunos = json.load(f)
    else:
        alunos = []

    novo_aluno = {
        "nome": input("Nome: "),
        "telefone": input("Telefone: "),
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: "),
        "id": input("qual ID desejado?: ")
    }
    
    alunos.append(novo_aluno)

    with open(dados_alunos, 'w', encoding='utf-8') as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)
        
    print("Aluno cadastrado com sucesso!")

def listar_aluno():
    print('==== lISTAR ALUNOS ====\n')
    if os.path.exists(dados_alunos):
        with open(dados_alunos, 'r', encoding='utf-8') as arquivo:
            alunos = json.load(arquivo)
    
    else:
        alunos = []

    if not alunos:
        print('a lista está vazia.')
        return
    
    for aluno in alunos:
        print(f" aluno: {aluno["nome"]} id: {aluno["id"]} idade: {aluno["idade"]} CPF: {aluno["cpf"]} telefone: {aluno["telefone"]} turma: {aluno["turma"]}")


def atualizar():
    print("\n ==== Atualizar Cadastro ====")
    if not os.path.exists(dados_alunos):
        print('a lista está vazia.')
        return

    with open(dados_alunos, 'r')as arquivo:
        alunos = json.load(arquivo)

    cpf = int(input("qual CPF do aluno que deseja atualizar?: "))

    for aluno in alunos:
        if aluno["cpf"] == cpf:
            print(f"alterando dados de {aluno["nome"]}")
            aluno["nome"] = input("qual o nome atualizado?: ")
            aluno["cpf"] = int(input("qual o CPF atualizado?: "))
            aluno["id"] = int(input("qual o id atualizado?: "))
            aluno["turma"] = int(input("qual a turma atualizada?: "))
            aluno["idade"] = int(input("qual a idade atualizada?: "))
            aluno["telefone"] = int(input("qual o telefone atualizado?: "))

            with open(dados_alunos, "w")as arquivo:
                json.dump(alunos)
            
            print("aluno atualizado com sucesso!")
        
        print("aluno não encontrado.")


def excluir():
    print("\n ==== Excluir Cadastro ====")
    if not os.path.exists(dados_alunos):
        print("a lista está vazia.")
    
    with open (dados_alunos, 'r') as arquivo:
        alunos = json.load(arquivo)

    cpf_busca = int(input("qual o CPF do aluno que deseja excluir?: "))

    for aluno in alunos:
        if aluno["cpf"] == cpf_busca:
            del aluno["cpf"]

        print("aluno não encontrado.")
    
    with open(dados_alunos, 'w', ) as arquivo:
        json.dump(alunos, arquivo, indent=4, ensure_ascii=False)
    
    print("aluno não encontrado.")


while True:
    print("\n ==== Menu do Usuário ====")
    print("1. cadastrar aluno")
    print("2. ver lista de alunos")
    print("3. atualizar aluno")
    print("4. excluir aluno")
    print("5. encerrar sistema")

    op = int(input("escolha uma opção: "))

    if op == 1: cadastrar()
    if op == 2: listar_aluno()
    if op == 3: atualizar()
    if op == 4: excluir()
    if op == 5: 
        print("encerrando sistema...")
        break
    else:
        print("opção inválida.")