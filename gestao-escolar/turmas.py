from escola import listar_escolas
from banco import conectar

def cadastrar_turmas():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()

        print("\n ==== SISTEMA DE CADASTRAMENTO DE TURMAS ====")
        print("ATENÇÃO! Só poderão ser cadastradas turmas com um ID_ESCOLA váldo.")

        nome_turma = input("digite o nome da turma: ").strip()
        id_escola = int(input("digite o ID da escola: "))

        cursor.execute('''SELECT id FROM escolas WHERE id = ?''', (id_escola, ))
        dados = cursor.fetchone()

        if not dados:
            print("\n id inválido!")
            return
        
        else:
            cursor.execute('''INSERT INTO turmas (nome_turma, id_escola) VALUES (?, ?)''', (nome_turma, id_escola))

            conexao.commit()

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
SELECT escolas.nome_escola, escolas.id, escolas.cidade_escola, turmas.nome_turma, turmas.id_escola FROM turmas LEFT JOIN escolas ON turmas.id_escola = escolas.id''')
        
        turmas = cursor.fetchall()

        if not turmas:
            print("não há registros.")
            return
        
        listar_escolas()
        
        for registros in turmas:
                nome_escola, id, cidade_escola, nome_turma, id_escola = registros

                print(f"nome turma: {nome_turma};")
                print(f"nome da escola relacionada: {nome_escola}; ID escola relacionada: {id};")
                print(f"cidade escola: {cidade_escola}; id: {id_escola}")
        
        return "certo"
    finally:
        conexao.close()