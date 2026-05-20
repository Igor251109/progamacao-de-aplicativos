#  A secretaria de uma escola precisa aposentar as fichas de papel e utilizar um sistema digital.
# Você foi designado para criar o protótipo desse sistema usando Python e armazenamento em arquivos JSON.

# Objetivo:
# Desenvolver um CRUD completo (Criar, Ler, Atualizar e Deletar) para gerenciar o cadastro de alunos, garantindo que os dados não sejam perdidos ao fechar o programa.


import json 


def cadastrar_aluno():
    dados = {"cpf": int(input("digite seu CPF: ")),
             "nome": input("digite seu nome completo: "),
             "telefone": int(input("digite seu telefone: ")),
             "turma": int(input("qual sua turma?: ")),
             "idade": int(input("digite sua idade: "))}

    with open("crud.json", 'a') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    print("aluno registrado com suceso!")


def listar_aluno():
    with open("crud.json", 'r') as arquivo:
        dados = json.load(arquivo)
    
    n = 0
    for alunos in dados:
        if dados == 0:
            print("A lista está vazia.")
        print(f"{n} - {alunos["nome"]}/CPF: {alunos["cpf"]}/idade: {alunos["idade"]}/ telefone: {alunos["telefone"]}/ Turma: {alunos["turma"]}")
        n += 1


