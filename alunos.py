# Contexto: A secretaria da escola aprovou o banco de dados que o professor criou.
# Agora, sua missão como programador é criar um sistema interativo que converse com o usuário através do terminal,
# colete as informações de um novo aluno e salve tudo dentro do arquivo escola_demonstracao.db
# usando o comando INSERT com F-Strings.

import sqlite3
conexao = sqlite3.connect('escola_demostracao.db')
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute ('''create table if not exists alunos (
        id_aluno INTEGER primary key autoincrement,
        nome_aluno TEXT not null,
        telefone_aluno TEXT not null,
        turma_aluno TEXT,
        idade_aluno INTEGER not null,
        cpf_aluno TEXT not null,
        id_professor_responsavel INTEGER not null,
        
        FOREIGN KEY (id_professor_responsavel) REFERENCES professores (id_professor)
    )''')


def registrar_alunos():    # registrar novos alunos no banco de dados.
    print("\n ==== REGISTRAR ALUNO ====")

    nome = input("qual o nome completo do aluno? (obrigatório): ")
    telefone = input("qual o telefone do aluno? (obrigatório): ")
    turma = input("qual a turma do aluno? (opcional): ")
    idade = int(input("qual a idade do aluno? (obrigatório): "))
    cpf = input("qual o CPF do aluno? (obrigatório): ")
    id_prof = int(input("qual o ID do professor responsável? (obrigatório): "))

    comando_inserir = f'''insert into alunos (nome_aluno, telefone_aluno, turma_aluno, idade_aluno, cpf_aluno, id_professor_responsavel)
    values ('{nome}', '{telefone}', '{turma}', {idade}, '{cpf}', {id_prof})'''

    cursor.execute(comando_inserir)
    conexao.commit()

    print("aluno registrado com sucesso!")


def ver_alunos():      # ver alunos no banco de dados.
    cursor.execute("SELECT * FROM alunos")
    dados = cursor.fetchall()

    print("\n ==== ALUNOS REGISTRADOS ====")

    for aluno in dados:
        print(f"alunos: {aluno} | professor: ")


def atualizar_alunos():      # atualizar alunos no banco de dados
    ver_alunos()

    print("\n ==== ATUALIZAR ALUNOS ====")
    qual_mudar = int(input("qual ID do aluno que quer atualizar?: "))

    cursor.execute(
        "SELECT * FROM alunos WHERE id_aluno = ?", (qual_mudar,)
    )

    aluno = cursor.fetchone()

    if aluno:
        novo_nome = input("qual o novo nome do aluno?: ")
        novo_cpf = input("qual é o novo CPF do aluno?: ")
        nova_idade = int(input("qual a nova idade?: "))
        novo_telefone = input("qual o novo telefone?: ")
        nova_turma = input("qual a nova turma do aluno?: ")

        cursor.execute(
            "UPDATE alunos SET nome_aluno = ?, cpf_aluno = ?, telefone_aluno = ?, turma_aluno = ?, idade_aluno = ? WHERE id_aluno = ?",
              (novo_nome, novo_cpf, novo_telefone, nova_turma, nova_idade, qual_mudar)
        )

        conexao.commit()

        print("Aluno atualizado com sucesso!")
    
    else:
        print("Aluno não encontrado.")


def deletar_aluno():       # deletar alunos do banco de dados
    print("\n ==== DELETAR ALUNO ====")
    ver_alunos()

    qual_deletar = int(input("qual ID do aluno que deseja deletar?: "))

    cursor.execute(
            "DELETE FROM alunos WHERE id_aluno = ?", (qual_deletar,)
    )
    conexao.commit()

    print("aluno removido com sucesso!")
    

while True:
    print("\n ==== MENU DE INTERAÇÃO ====")
    print("1 - adicionar alunos / 2 - ver alunos / 3 - atualizar alunos / 4 - deletar aluno | 5 - sair")
    op = int(input("qual opção vai escolher?: "))

    if op == 1: registrar_alunos()
    elif op == 2: ver_alunos()
    elif op == 3: atualizar_alunos()
    elif op == 4: deletar_aluno()
    elif op == 5:
        print("encerrando programa...")
        break
    else:
        print("opção invalida.")

conexao.close()