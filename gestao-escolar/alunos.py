from turmas import listar_turmas
from banco import conectar

def cadastrar_alunos():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()

        print("\n ==== SISTEMA DE CADASTRAMENTO DE ALUNOS ====")
        print("\n ATENÇÃO! Só será possivel adicionar alunos a um ID_TURMA válido.")

        nome = "Igor"
        idade = 16
        id_turma = 1

        cursor.execute('''SELECT id FROM turmas WHERE ID = ?''', (id_turma, ))
        dados = cursor.fetchone()

        if dados is None:
            print("\n ID_TURMA inválido. tente novamente.")
            return
        
        else:
            cursor.execute('''INSERT INTO alunos (nome, idade, id_turma) VALUES (?, ?, ?)''', (nome, idade, id_turma))

            conexao.commit()

            print("certo")
            return "certo"
        
    finally:
        conexao.close()

def listar_alunos():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()
        print("\n ==== LISTAGEM DE ALUNOS E TURMAS RELACIONADAS ====")

        cursor.execute('''
            SELECT alunos.nome, alunos.idade, alunos.id_turma, turmas.id, turmas.nome_turma FROM alunos LEFT JOIN turmas ON alunos.id_turma = turmas.id ORDER BY alunos.id''')
        dados = cursor.fetchall()

        if not dados:
            print("não há registros.")
            return

        listar_turmas()
        for alunos in dados:
            print(f"ID: {alunos[0]} | Nome: {alunos[1]} | Idade: {alunos[2]} | ID Turma: {alunos[3]}")
            print("-" * 30)

        print("certo")
        return "certo"
    finally:
        conexao.close()