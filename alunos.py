# Contexto: A secretaria da escola aprovou o banco de dados que o professor criou.
# Agora, sua missão como programador é criar um sistema interativo que converse com o usuário através do terminal,
# colete as informações de um novo aluno e salve tudo dentro do arquivo escola_demonstracao.db
# usando o comando INSERT com F-Strings.

import sqlite3
conexao = sqlite3.connect('escola_demostracao.db')
cursor = conexao.cursor()

cursor.execute ('''CREATE TABLE IF NOT EXISTS alunos (
        id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_aluno TEXT NOT NULL,
        telefone_aluno TEXT NOT NULL,
        turma_aluno TEXT,
        idade_aluno INTEGER NOT NULL,
        cpf_aluno TEXT NOT NULL,
        id_professor_responsavel INTEGER NOT NULL,
        endereco TEXT,
        
        FOREIGN KEY (id_professor_responsavel) REFERENCES professores (id_professor)
    )''')


def registrar_alunos():    # registrar novos alunos no banco de dados.
    print("\n ==== REGISTRAR ALUNO ====")

    try:
        nome = input("qual o nome completo do aluno? (obrigatório): ")
        telefone = input("qual o telefone do aluno? (obrigatório): ")
        turma = input("qual a turma do aluno? (opcional): ")
        idade = int(input("qual a idade do aluno? (obrigatório): "))
        cpf = input("qual o CPF do aluno? (obrigatório): ")
        endereco = input("qual o endereço do aluno? (opcional): ")
        id_prof = int(input("qual o ID do professor responsável? (obrigatório): "))
    

        comando_inserir = f'''insert into alunos (nome_aluno, telefone_aluno, turma_aluno, idade_aluno, cpf_aluno, endereco, id_professor_responsavel)
        values ('{nome}', '{telefone}', '{turma}', {idade}, '{cpf}', '{endereco}', {id_prof})'''

        cursor.execute(comando_inserir)
        conexao.commit()

    except ValueError:
        print("Erro: digite as informações de maneira correta.")
        return
    except sqlite3.IntegrityError:
        print("ERROR: Campo obrigatório não preenchido / Dados unicos já existentes")

    print("aluno registrado com sucesso!")


def ver_alunos():      # ver alunos no banco de dados.
    try:
        cursor.execute("SELECT * FROM alunos")
        dados = cursor.fetchall()

        print("\n ==== ALUNOS REGISTRADOS ====")

        for aluno in dados:
            print(f"alunos: {aluno}")
    except sqlite3.OperationalError:
        print("ERROR: erro no banco de dados (verefique se esta aberto).")


def atualizar_alunos():      # atualizar alunos no banco de dados
    ver_alunos()

    print("\n ==== ATUALIZAR ALUNOS ====")
    try:
        qual_mudar = int(input("qual ID do aluno que quer atualizar?: "))

        cursor.execute(
            "SELECT * FROM alunos WHERE id_aluno = ?", (qual_mudar,)
        )

        aluno = cursor.fetchone()

        if not aluno:
            print("o aluno não existe")
            return

        elif aluno:
            novo_nome = input("qual o novo nome do aluno? (obrigatório): ")
            novo_cpf = input("qual é o novo CPF do aluno? (obrigatório): ")
            nova_idade = int(input("qual a nova idade? (obrigatório): "))
            novo_telefone = input("qual o novo telefone? (obrigatório): ")
            nova_turma = input("qual a nova turma do aluno? (opcional): ")
            novo_endereco = input("qual o novo endereço do aluno? (opcional): ")
    except ValueError:
        print("ERROR: digite as informações de maneira correta.")
        return

    try:
        cursor.execute(
                "UPDATE alunos SET nome_aluno = ?, cpf_aluno = ?, telefone_aluno = ?, turma_aluno = ?, idade_aluno = ?, endereco = ? WHERE id_aluno = ?",
                (novo_nome, novo_cpf, novo_telefone, nova_turma, nova_idade, novo_endereco, qual_mudar))
        
        print("Aluno atualizado com sucesso!")

        conexao.commit()
    except sqlite3.OperationalError:
        print("ERROR: dados duplicados / espaços obrigatório nao preenchido")
    except sqlite3.IntegrityError:
        print("ERROR: erro no banco de dados.")


def deletar_aluno():       # deletar alunos do banco de dados
    print("\n ==== DELETAR ALUNO ====")
    ver_alunos()

    try:
        qual_deletar = int(input("qual ID do aluno que deseja deletar?: "))
    except ValueError:
        print("ERROR: digite um número valido.")
        return

    try:
        cursor.execute(
                "DELETE FROM alunos WHERE id_aluno = ?", (qual_deletar,)
        )
        conexao.commit()

        print("aluno removido com sucesso!")
    except sqlite3.OperationalError:
        print("ERROR: erro no banco de dados. verefique o codigo SQL.")


def menu():
    op = 0
    while op != 5:
        print("\n ==== MENU DE INTERAÇÃO ====")
        print("1 - adicionar alunos / 2 - ver alunos / 3 - atualizar alunos / 4 - deletar aluno | 5 - sair")
        try:
            op = int(input("qual opção vai escolher?: "))
        except ValueError:
            print("ERROR: digite um numero valido.")
            continue

        if op == 1: registrar_alunos()
        elif op == 2: ver_alunos()
        elif op == 3: atualizar_alunos()
        elif op == 4: deletar_aluno()
        elif op == 5:
            print("-" * 30)
            print("encerrando programa...")
                
        else:
            print("opção invalida.")

menu()
conexao.close()