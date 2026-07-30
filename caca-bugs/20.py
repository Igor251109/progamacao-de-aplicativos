#            import sqlite3 
 
#            def cadastrar_escola_manual(): 
            	# O aluno resolveu gerar o ID por conta própria 
#                id_escola = int(input("Digite o ID para a nova escola: ")) 
#            	nome = input("Nome da escola: ") 
     
#                conexao = sqlite3.connect('sistema_escola.db') 
#            	cursor = conexao.cursor() 
     
            	# Se rodar duas vezes com o ID 1, o programa fecha abruptamente (Crash). 
            	# Aplique a blindagem protetora necessária: 
#                cursor.execute("INSERT INTO escolas (id, nome) VALUES (?, ?)", (id_escola, nome)) 
     
#                conexao.commit() 
#                conexao.close()

#             RESOLUÇÃO:

import sqlite3 
conexao = sqlite3.connect('sistema_escola.db') 
cursor = conexao.cursor()
 
def cadastrar_escola_manual():
    try:

        id_escola = int(input("Digite o ID para a nova escola: ")) 
        nome = input("Nome da escola: ") 

        cursor.execute('''CREATE TABLE IF NOT EXISTS escolas (
                    id INTEGER PRIMARY KEY,
                    nome TEXT
                    )
                    ''') 

        cursor.execute(f"SELECT * FROM escolas WHERE id = {id_escola}")

        if cursor.fetchone() == id_escola:
            print("o ID já existe!")
            return

        cursor.execute("INSERT INTO escolas (id, nome) VALUES (?, ?)", (id_escola, nome)) 
        
        conexao.commit() 


    except sqlite3.IntegrityError:
        print("ERROR: Erro de integridade.")
        return

def menu():
    while True:
        print("\n ==== MENU ====")
        print("1. Cadastro")
        print("2. sair")
        
        escolha = int(input("qual opção vais escolher?: "))

        if escolha == 1: cadastrar_escola_manual()
        elif escolha == 2:
            print("encerrando...")
            break
        else:
            print("dado inválido.")
            return
        
menu()
conexao.close()