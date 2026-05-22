import json              # prepara o arquivo no formato json.
import os                #  interagir com o sistema operacional, como verificar arquivos e pastas.

BANCO_DADOS = 'alunos.json'                 # cria o arquivo e salva na váriavel "BANCO_DADOS".

def cadastrar():                   # cria uma função para cadastrar os alunos.
    print("\n--- Novo Cadastro ---")               # mostra a mensagem "novo cadastro"

    if os.path.exists(BANCO_DADOS):                # se o arquivo existir:
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:                 # abra no modo de leitura, permita acentos e salve na váriavel "f".
            alunos = json.load(f)                   # lê todo o arquivo e salva na váriavel "alunos".
    else:                # se o arquivo não existir:
        alunos = []            # cria uma lista 

    novo_aluno = {                # cria um dicionário para pegar as informações dos alunos.
        "nome": input("Nome: "),            # cria uma chave: "nome" e pergunta o nome do aluno.
        "telefone": input("Telefone: "),              # cria uma chave: "telefone" e pergunta o telefone do aluno.
        "turma": input("Turma: "),            # cria uma chave: "turma" e pergunta a turma do aluno.
        "idade": int(input("Idade: ")),               # cria uma chave: "idade" e pergunta a idade do aluno.
        "cpf": input("CPF: ")            # cria uma chave: "cpf" e pergunta o CPF do aluno.
    }           # fecha o dicionário

    alunos.append(novo_aluno)                # adiciona as informações do aluno na lista "alunos".

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f:              # abrir o arquivo no modo sobrescrever, permitindo acentos e salvando na variável "f".
        json.dump(alunos, f, indent=4, ensure_ascii=False)              # escrever as informações no arquivo permitindo acentos e escrevendo de forma organizada.

    print("Aluno cadastrado com sucesso!")              # mostrar a mensagem "aluno cadastrado com sucesso!".

def listar():             # cria uma função para mostrar os alunos que estão na lista.
    print("\n--- Lista de Alunos ---")               # mostrar a mensagem "lista de alunos".

    if os.path.exists(BANCO_DADOS):                # se o arquivo existir:
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:             # abra o rquivo no modo leitura, permitindo acentos e salve na váriavel "f".
            alunos = json.load(f)                 # leia o arquivo e salve na váriavel "alunos".
    else:                 # se o arquivo não existir:
        alunos = []                 # cria uma lista no arquivo.

    if not alunos:                # se não tiver alunos na lista:
        print("Nenhum aluno cadastrado.")              # mostrar a mensagem "nenhum aluno cadastrado."
        return               # salve a mensagem no arquivo

    for aluno in alunos:               # para cada aluno na lista de alunos:
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")  #mostrar as informações de cada aluno.

def atualizar():                # cria uma função para atualizar informações de alunos que estejam cadastrados.
    print("\n--- Atualizar Aluno ---")               # mostra a mensagem " atualizar aluno".
    if not os.path.exists(BANCO_DADOS):                 # se o arquivo não existir:
        print("Nenhum aluno cadastrado no sistema.")              # mostrar a mensagem "nenhum aluno cadastrado no sistema".
        return                 # salve a mensagem em uma váriavel.

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:               # abrir o arquivo no modo de leitura, permitindo acentos e salvando na váriavel "f".
        alunos = json.load(f)                # lê o arquivo e salva na váriavel "alunos"

    cpf_busca = input("Digite o CPF do aluno que deseja editar: ")                 # pergunta qual o CPF do aluno que vai ser editado no sistema.

    for aluno in alunos:                # para cada aluno na lista de alunos:
        if aluno['cpf'] == cpf_busca:               # se o cpf do aluno for igual a cpf pedido pra editar:
            print(f"Editando dados de: {aluno['nome']}")                        # mostra a mensagem "editando dads do aluno"
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']                    # pergunta qual vai ser o novo nome do aluno que está sendo atualizado.
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']               # pergunta o novo telefone do aluno que está sendo atulizado.
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']                             # pergunta a nova turma do luno que está sendo atualizado.
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])                   # pergunta a idade do aluno que está sendo atualizado.
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']                          # pergunta o cpf do aluno que está sendo atualizado.
 
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:                            # abra o arquivo no modo sobrescrever, permitindo acentos e salve na váriavel "f".
                json.dump(alunos, f, indent=4, ensure_ascii=False)                      #  escreve os dados atualizados no arquivo, de forma organizada e permitindo acentos.
            print("Dados atualizados com sucesso!")                    # mostra a mensagem "dados atualizados com sucesso!"
            return               # salva a mensagem no arquivo.

    print("Aluno não encontrado.")                       # se o CPF procurado não for encontrado, mostre a mensagem: "aluno não encontrado.".

def excluir():                          # cria uma função para excluir um aluno cadastrado no sistema.
    print("\n--- Excluir Aluno ---")                           #mostra a mensagem: "excluir aluno"
    if not os.path.exists(BANCO_DADOS):               # se o arquivo não existir existir:
        print("Nenhum aluno cadastrado no sistema.")                 # mostrar a mensagem: "nenhum aluno cadastrado no sistema.".
        return  "salva a mensagem"

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:                       # se o arquivo existir: abra ele no modo leitura, permitindo acentos e salve na váriavel "f".
        alunos = json.load(f)                     # leia o arquivo e salve na váriavel "alunos".

    id_busca = int(input("Digite o ID do aluno que deseja remover: "))                   # pergunta o ID do aluno que deseja excluir
    cpf_busca = input("Digite o cpf do aluno que deseja remover: ")                     # pergunta o CPF do aluno que deseja excluir.

    nova_lista = [a for a in alunos if a['id'] != id_busca]                    # cria uma nova lista: Para cada aluno na lista Se o ID for diferente do id de exclusão.
    nova_lista = [a for a in alunos if a['cpf'] != cpf_busca]                     # cria uma lista; Para cada aluno na lista Se o CPF for diferente de cpf de exclusão.

    if len(nova_lista) < len(alunos):                      # ler a lista criada: se a lista criada for menor que a lista "alunos":
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:                       # abra o arquivo no modo sobrescrever, permitindo centos e salve na váriável "f".
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)                 # escreva a informações já com a exclusão do aluno, de forma organizada e permitindo acentos.
        print("Aluno removido com sucesso!")                 # mostrar a mensagem: "aluno removido com sucesso."
    else:                     #se a lista não for menor que a lista alunos:
        print("Aluno não encontrado.")                     # mostrar a mensagem: "aluno não encontrado"

def menu():                  # criar uma função do menu para o usuário.
    if not os.path.exists(BANCO_DADOS):                     # se o arquivo não existir:
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:                  # abra o arquivo no modo sobrescrever, permitindo acentos e salve na váiavel "f".
            json.dump([], f)              # escreva as informações na da variável na lista.

    while True:                  # enquanto for verdadeiro:
        print("\n=== SISTEMA ESCOLAR ===")               # mostrar a mensagem: "sistema escolar"
        print("1. Cadastrar Aluno")               # mostrar a mensagem: "1. cadastrar aluno"
        print("2. Listar Alunos")                # mostrar a mensagem: "2. listar alunos"
        print("3. Atualizar Aluno")                # mostrar a mensagem: "3. atualizar aluno"
        print("4. Excluir Aluno")              # mostrar a mensagem: "4. excluir aluno"
        print("5. Sair")             # mostrar a mensagem: "5. sair"

        opcao = input("Escolha uma opção: ")                # pergunta qual opção o usuário vai querer usar.

        if opcao == '1': cadastrar()                 # se o usuário escolher a opção 1, chame a função "cadastrar()"
        elif opcao == '2': listar()                 # se o usuário escolher a opção 2, chame a função "listar()"
        elif opcao == '3': atualizar()                # se o usuário escolher a opção 3, chame a função "atualizar()"
        elif opcao == '4': excluir()                # se o usuário escolher a opção 4, chame a função "excluir()"
        elif opcao == '5': break                  # se o usuário escolher a opção 5, pare o sistema.
        else: print("Opção inválida!")              # mostre a mensagem: "opção inválida!"

menu()