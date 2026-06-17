import sqlite3
conexao = sqlite3.connect('escola_demostracao.db')
cursor = conexao.cursor()

# Criar uma tabela "profesores" no banco de dados
cursor.execute('''create table if not exists professores (
               id_professor integer primary key autoincrement,
               nome_professor text not null,
               telefone_professor text not null,
               materia_professor text,
               idade_professor integer not null,
               cpf_professor text not null,
               salario_professor text,
               nome_colegio text
               ) ''' )

def registrar_professores():    # registrar professores no banco de dados
    print("\n ==== REGISTRAR PROFESSORES ====")
    nome = input("Qual o nome completo do professor? (obrigatório): ")
    telefone = input("Qual o telefone do professor? (obrigatório): ")
    materia = input("Qual a matéria do professor? (opcional): ")
    idade = int(input("Qual a idade do professor?(obrigatório): "))
    cpf = input("qual o CPF do professor? (obrigatório): ")
    salario = input("qual o salário atual do professor? (opcional): ")
    nome_colegio = input("qual o nome do colégio? (obrigatório): ")

    comando_inserir = f'''INSERT into professores (nome_professor, telefone_professor, materia_professor, idade_professor, cpf_professor, salario_professor, nome_colegio)
     values ('{nome}', '{telefone}', '{materia}', {idade}, '{cpf}', '{salario}', '{nome_colegio}') '''
    
    cursor.execute(comando_inserir)
    print("professor registrado com sucesso!")
    conexao.commit()

def ver_professores():
    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()

    print("\n ==== PROFESSORES REGISTRADOS ==== ")

    for professor in professores:
        print(professor)

def atualizar_professores():    # Atualizar professores já registrados no banco de dados.
    ver_professores()

    print("\n ==== ATUALIZAR PROFESSORES ====")
    
    id_professor = int(input("qual o ID do professor que deseja atualizar?: "))

    cursor.execute(f"SELECT * FROM professores WHERE id_professor = {id_professor}")

    professor = cursor.fetchone()

    if not professor:
        print("não encontrado.")
        conexao.close()
        return
    
    else:
        nome = input("Qual o nome completo do professor? (obrigatório): ")
        telefone = input("Qual o telefone do professor? (obrigatório): ")
        materia = input("Qual a matéria do professor? (opcional): ")
        idade = int(input("Qual a idade do professor?(obrigatório): "))
        cpf = input("qual o CPF do professor? (obrigatório): ")
        salario = input("qual o salário atual do professor? (opcional): ")
        nome_colegio = input("qual o nome do colégio? (obrigatório): ")

        cursor.execute(
            "UPDATE professores SET nome_professor = ?, telefone_professor = ?, materia_professor = ?, idade_professor = ?, cpf_professor = ?, salario_professor = ?, nome_colegio = ? WHERE id_professor = ?",
            (nome, telefone, materia, idade, cpf, salario, nome_colegio, id_professor )
        ) 

        print("professor atualizado com sucesso!")
        conexao.commit()

def deletar_professores():    # Deletar professores já registados no banco de dados.
    ver_professores()

    print("\n ==== EXCLUIR PROFESSORES ====")

    idx = int(input("qual o ID do professor que deseja excluir?: "))

    cursor.execute(
        "DELETE FROM professores WHERE id_professor = ?", (idx,)
    )

    print("professor excluido com sucesso!")

    conexao.commit()

def menu():     # Menu de interação com o usário.
    while True:
        print("\n ==== MENU DO USUÁRIO ====")
        print("1 - Registrar Professores")
        print("2 - Ver Professores Registrados")
        print("3 - Atualizar Informações de Professores")
        print("4 - Deletar Professores Registrados")
        print("5 - sair")

        opcao = int(input("Qual opção vai escolher?: "))

        if opcao == 1: registrar_professores()
        elif opcao == 2: ver_professores()
        elif opcao == 3: atualizar_professores()
        elif opcao == 4: deletar_professores()
        elif opcao == 5:
            print("encerrando sistema...")
            conexao.close()
            break

menu()