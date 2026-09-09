from banco import conectar

def cadastrar_escolas():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()
        print("\n ==== SISTEMA DE CADASTRAMENTO DE ESCOLAS ====")

        nome_escola = "Sesi Paranavaí"
        cidade_escola = "Paranavaí"

        cursor.execute('''INSERT INTO escolas (nome_escola, cidade_escola) VALUES (?, ?)''', (nome_escola, cidade_escola))

        conexao.commit()

        print("certo")
        return "certo"
    finally:
        conexao.close()

def listar_escolas():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()

        print("\n ==== LISTAGEM DE ESCOLAS ====")

        cursor.execute('''SELECT * FROM escolas ORDER BY id''')
        dados = cursor.fetchall()

        if not dados:
            print("não há nenhuma escola no sistema.")
            return
        
        for escolas in dados:
            print(f"ID: {dados[0]} | Nome escola: {dados[1]} | Cidade Escola: {dados[2]}")
            print("-" * 30)

        print("certo")
        return "certo"
    
    finally:
        conexao.close()