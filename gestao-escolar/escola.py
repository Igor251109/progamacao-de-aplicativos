from banco import conectar

def cadastrar_escolas():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()
        print("\n ==== SISTEMA DE CADASTRAMENTO DE ESCOLAS ====")

        nome_escola = input("digite o nome da escola: ").strip()
        cidade_escola = input("digite a cidade da cidade: ").strip()

        cursor.execute('''INSERT INTO escolas (nome_escola, cidade_escola) VALUES (?, ?)''', (nome_escola, cidade_escola))

        conexao.commit()

        return "certo"
    finally:
        conexao.close()

def listar_escolas():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()

        print("\n ==== LISTAGEM DE ESCOLAS ====")

        cursor.execute('''SELECT * FROM escolas''')
        dados = cursor.fetchall()

        for escolas in dados:
            print(escolas)
        
        return "certo"
    
    finally:
        conexao.close()