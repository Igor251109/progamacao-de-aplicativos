#  A secretaria de uma escola precisa aposentar as fichas de papel e utilizar um sistema digital.
# Você foi designado para criar o protótipo desse sistema usando Python e armazenamento em arquivos JSON.

# Objetivo:
# Desenvolver um CRUD completo (Criar, Ler, Atualizar e Deletar) para gerenciar o cadastro de alunos, garantindo que os dados não sejam perdidos ao fechar o programa.

import json 


def cadastrar_aluno():     # cadrastar um novo aluno.
    dados = {
            "cpf": int(input("digite seu CPF: ")),
             "nome": input("digite seu nome completo: "),
             "telefone": int(input("digite seu telefone: ")),
             "turma": int(input("qual sua turma?: ")),
             "idade": int(input("digite sua idade: "))
             }
    try:
        with open("crud.json", 'r') as arquivo:
            lista = json.load(arquivo)
        print('-' * 50)
        lista.append(dados)
    
    except:
        lista = []
        lista.append(dados)

    with open("crud.json", 'w') as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)   
    print("aluno registrado com suceso!")


def listar_aluno():      # mostrar todos os alunos cadastrados.
    with open("crud.json", 'r') as arquivo:
        dados = json.load(arquivo)
    
    n = 0
    for alunos in dados:
        if alunos == 0:
            print("A lista está vazia.")
            break
        print(f"{n} - {dados[n]["nome"]}/CPF: {dados[n]["cpf"]}/idade: {dados[n]["idade"]}/ telefone: {dados[n]["telefone"]}/ Turma: {dados[n]["turma"]}")
        n += 1


def atualizar_aluno():    # atualizar as informações de algum cadastro.
    listar_aluno()
    print('-' * 50)

    qual_mudar = int(input('qual ID do aluno que quer mudar?: '))
    print('-' * 50)

    dados = {
            "cpf": int(input("digite seu CPF: ")),
             "nome": input("digite seu nome completo: "),
             "telefone": int(input("digite seu telefone: ")),
             "turma": int(input("qual sua turma?: ")),
             "idade": int(input("digite sua idade: "))
             }
    
    print('-' * 50)

    with open("crud.json", 'r') as arquivo:
        mudar = json.load(arquivo)

        mudar[qual_mudar] = dados

    with open("crud.json", 'w') as arquivo:
        json.dump(mudar, arquivo, indent=4, ensure_ascii=False)
    
    print('aluno atualizado com sucesso!')


def excluir_aluno():    # excluir algum aluno cadastrado.
    listar_aluno()
    print('-' * 50)

    qual_excluir = int(input('qual ID do aluno que quer excluir?: '))
    print('-' * 50)

    with open("crud.json", 'r') as arquivo:
        excluir = json.load(arquivo)

        del excluir[qual_excluir]
    
        with open("crud.json", 'w') as arquivo:
            json.dump(excluir, arquivo, indent=4, ensure_ascii=False)

    print("aluno excluido com sucesso!")


while True:
    print('-' * 50)
    print("1 - adicionar aluno | 2 - ver alunos | 3 - atualizar aluno | 4 - excluir aluno | 5 - sair")
    print('-' * 50)
    op = int(input("qual opção vai escolher?: "))
    print('-' * 50)

    if op == 1: cadastrar_aluno()
    elif op == 2: listar_aluno()
    elif op == 3: atualizar_aluno()
    elif op == 4: excluir_aluno()
    elif op == 5:
        print("encerrando sistema...")
        print('-' * 50)
        break