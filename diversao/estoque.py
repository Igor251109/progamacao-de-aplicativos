import sqlite3

def conectar():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    return conexao, cursor

def tratar_erros_funcoes(funcao):
    try:
        funcao()
    except ValueError:
        print("-" * 30)
        print("dados inválidos.")
        print("-" * 30)
        return
    except sqlite3.OperationalError:
        print("-" * 30)
        print("erro operacional no banco de dados.")
        print("-" * 30)
        return
    except sqlite3.IntegrityError:
        print("-" * 30)
        print("erro de integridade no banco de dados.")
        print("-" * 30)
        return
    except KeyboardInterrupt:
        print("-" * 30)
        print("encerrando sistema...")
        print("-" * 30)
        return

def criar_tabelas():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        quantidade INTEGER NOT NULL
        )
        ''')
        
        conexao.commit()
        
    finally:
        if conexao:
            conexao.close()

def adicionar_produtos():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()

        print("\n ==== ADICIONAR PRODUTOS ====")

        nome_produto = input("qual o nome do produto?: ")
        categoria = input("qual a categoria do produto?: ")
        quantidade = int(input("qual a quantidade atual do produto?"))

        cursor.execute("INSERT INTO produtos (nome, categoria, quantidade) VALUES (?, ?, ?)", (nome_produto, categoria, quantidade))

        conexao.commit()

        print("produto adicionado com sucesso!")
        return "certo"
    
    finally:
        if conexao:
            conexao.close()
