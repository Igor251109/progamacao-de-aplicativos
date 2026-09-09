from escola import listar_escolas
from banco import conectar

def cadastrar_turmas():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()

        print("\n ==== SISTEMA DE CADASTRAMENTO DE TURMAS ====")
        print("ATENÇÃO! Só poderão ser cadastradas turmas com um ID_ESCOLA váldo.")

        nome_turma = "2 ano"
        id_escola = 1

        cursor.execute('''SELECT id FROM escolas WHERE id = ?''', (id_escola, ))
        dados = cursor.fetchone()

        if not dados:
            print("\n id inválido!")
            return
        
        else:
            cursor.execute('''INSERT INTO turmas (nome_turma, id_escola) VALUES (?, ?)''', (nome_turma, id_escola))

            conexao.commit()

            print("certo")
            return "certo"
        
    finally:
        conexao.close()

def listar_turmas():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()

        print("\n ==== LISTAGEM DE ESCOLAS E TURMAS RELACIONADAS ====")

        cursor.execute('''
SELECT escolas.nome_escola, escolas.id, escolas.cidade_escola, turmas.nome_turma, turmas.id_escola FROM turmas LEFT JOIN escolas ON turmas.id_escola = escolas.id ORDER BY turmas.id''')
        
        turmas = cursor.fetchall()

        if not turmas:
            print("não há registros.")
            return
        
        listar_escolas()
        for turma in turmas:
            print(f"ID: {turma[0]} | Nome Turma: {turma[1]} | ID Escola: {turma[2]}")
            print("-" * 30)
        
        return "certo"
    finally:
        conexao.close()