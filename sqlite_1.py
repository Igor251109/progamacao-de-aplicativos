# Contexto: A secretaria da escola aprovou o banco de dados que o professor criou.
# Agora, sua missão como programador é criar um sistema interativo que converse com o usuário através do terminal,
# colete as informações de um novo aluno e salve tudo dentro do arquivo escola_demonstracao.db
# usando o comando INSERT com F-Strings.

import sqlite3
conexao = sqlite3.connect('escola_demostracao.db')
cursor = conexao.cursor()

cursor.execute ('''create table if not exists alunos (
        id_aluno integer primary key autoincrement,
        nome_aluno text not null,
        telefone_aluno text not null,
        turma_aluno text,
        idade_aluno integer not null,
        cpf_aluno text not null
    )''')


def registrar_alunos():
    print("\n ==== REGISTRAR ALUNO ====")

    nome = input("qual o nome completo do aluno?: ")
    telefone = input("qual o telefone do aluno?: ")
    turma = input("qual a turma do aluno?: ")
    idade = int(input("qual a idade do aluno? (opcional): "))
    cpf = input("qual o CPF do aluno?: ")

    comando_inserir = f'''insert into alunos (nome_aluno, telefone_aluno, turma_aluno, idade_aluno, cpf_aluno)
    values ('{nome}', '{telefone}', '{turma}', '{idade}', '{cpf}')'''

    cursor.execute(comando_inserir)
    conexao.commit()

    print("aluno registrado com sucesso!")


def ver_alunos():
    cursor.execute("SELECT * FROM alunos")
    dados = cursor.fetchall()

    print("\n ==== ALUNOS REGISTRADOS ====")

    for aluno in dados:
        print(aluno)


def atualizar_alunos():
    print("\n ==== ALUNOS REGISTRADOS ====")
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

        cursor.execute(
            "UPDATE alunos SET nome_aluno = ?, cpf_aluno = ? WHERE id_aluno = ?", (novo_nome, novo_cpf, qual_mudar)
        )

        conexao.commit()

        print("Aluno atualizado com sucesso!")
    
    else:
        print("Aluno não encontrado.")


def deletar_aluno():
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