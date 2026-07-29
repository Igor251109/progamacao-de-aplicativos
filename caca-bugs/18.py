#            import sqlite3 
 
#            def cadastrar_lista_alunos(): 
#            	lista = [("Ana", 1), ("Carlos", 1), ("Beatriz", 2)] 
     
#                conexao = sqlite3.connect('sistema_escola.db') 
#            	cursor = conexao.cursor() 
     
            	# O comando executemany quebra com a mensagem: "function takes exactly 2 arguments". 
                	# Como passar a lista de dados da forma correta dentro dele? 
#                cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", lista) 
     
#                conexao.commit() 
#                conexao.close()


import sqlite3 
 
def cadastrar_lista_alunos(): 
    lista = [("Ana", 1), ("Carlos", 1), ("Beatriz", 2)] 

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   id_turma INTEGER)''')
	
    # O comando executemany quebra com a mensagem: "function takes exactly 2 arguments". 
	# Como passar a lista de dados da forma correta dentro dele? 
    cursor.executemany("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", lista)
     
    conexao.commit() 
    print("adicionado")
    conexao.close()

cadastrar_lista_alunos()

resposta = "o 'cursor.execute' só aceita um valor ou tupla. o 'executemany' aceita varios."