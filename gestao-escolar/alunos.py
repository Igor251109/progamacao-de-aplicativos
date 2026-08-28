from turmas import listar_turmas
from banco import conectar

def cadastrar_alunos():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()

        print("\n ==== SISTEMA DE CADASTRAMENTO DE ALUNOS ====")
        print("\n ATENÇÃO! Só será possivel adicionar alunos a um ID_TURMA válido.")

        nome = input("digite seu nome: ")
        idade = int(input("digite sua idade: "))
        id_turma = int(input("qual ID da turma relacionada?: "))

        cursor.execute('''SELECT id FROM turmas WHERE ID = ?''', (id_turma, ))
        dados = cursor.fetchone()

        if dados is None:
            print("\n ID_TURMA inválido. tente novamente.")
            return
        
        else:
            cursor.execute('''INSERT INTO alunos (nome, idade, id_turma) VALUES (?, ?, ?)''', (nome, idade, id_turma))

            conexao.commit()

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
            SELECT alunos.nome, alunos.idade, alunos.id_turma, turmas.id, turmas.nome_turma FROM alunos LEFT JOIN turmas ON alunos.id_turma = turmas.id''')
        dados = cursor.fetchall()

        if not dados:
            print("não há registros.")
            return

        listar_turmas()
        for aluno in dados:
            nome, idade, id_turma, id, nome_turma = aluno

            print(f"nome do aluno: {nome}; idade do aluno: {idade};")
            print(f"turma relacionada (id): {id}; id_turma: {id_turma}; nome da turma: {nome_turma}")
        
        return "certo"
    finally:
        conexao.close()