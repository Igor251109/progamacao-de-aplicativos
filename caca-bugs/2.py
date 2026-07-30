import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''CREATE TABLE IF NOT EXISTS escolas (
                   id_escola INTEGER PRIMARY KEY
                   )
                   ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS series (
                   nome_serie TEXT,
                   id_escola INTEGER,
                   FOREIGN KEY (id_escola) REFERENCES escolas(id_escola)
                   )
                   ''')

    try:
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)", (nome_serie, id_escola))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("erro: Escola inexistente!")
    finally:
        conexao.close()

def menu():
    while True:
        print("\n ==== MENU ====")
        print("1. Cadastro")
        print("2. sair")
        
        escolha = int(input("qual opção vais escolher?: "))

        if escolha == 1: 
            nome_serie = input("qual o nome da série que deseja adicionar?: ")
            id_escola = int(input("qual o ID da escola qu deseja atualizar?: "))
            cadastrar_serie(nome_serie, id_escola)
        elif escolha == 2:
            print("encerrando...")
            break
        else:
            print("dado inválido.")
            return

menu()



#            import sqlite3 
 
#            def cadastrar_serie(nome_serie, id_escola): 
#                conexao = sqlite3.connect('sistema_escola.db') 
#            	cursor = conexao.cursor() 
            	# O aluno tenta cadastrar uma série com id_escola = 999 (que não existe). 
            	# O SQLite aceita o cadastro mesmo assim. O que está faltando ativar? 
#                try: 
#                    cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)", (nome_serie, id_escola)) 
#                    conexao.commit() 
#                except sqlite3.IntegrityError: 
#                    print("Erro: Escola inexistente!") 
#                finally: 
#                    conexao.close()