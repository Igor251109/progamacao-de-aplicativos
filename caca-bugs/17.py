#            import sqlite3 
 
#            def inserir_professor(nome, materia, cpf): 
#                try: 
#                    conexao = sqlite3.connect('sistema_escola.db') 
#                	cursor = conexao.cursor() 
                	# Existe um erro de digitação no comando SQL (INSERTO).  
                	# Por que o programa mostra "CPF já cadastrado" em vez de avisar sobre o erro de sintaxe? 
#                    cursor.execute("INSERTO INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf)) 
#                    conexao.commit() 
#                except sqlite3.Error: 
#                    print("Erro: Este CPF já está cadastrado no sistema!") 
#                finally: 
#                conexao.close()

import sqlite3 
 
def inserir_professor(nome, materia, cpf): 
    try: 
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 

        cursor.execute('''CREATE TABLE IF NOT EXISTS professores (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT,
                       cpf TEXT UNIQUE,
                       materia TEXT
                       )
                       ''')
    	# Existe um erro de digitação no comando SQL (INSERTO).  
    	# Por que o programa mostra "CPF já cadastrado" em vez de avisar sobre o erro de sintaxe? 
        cursor.execute("INSERT INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf)) 
        conexao.commit() 
    except sqlite3.Error: 
        print("Erro: Este CPF já está cadastrado no sistema!") 
    finally: 
        conexao.close()

nome = "igor"
materia = "matematica"
cpf = "136.520.259-38"

inserir_professor(nome, materia, cpf)

resposta = "o comando 'except sqlite3.error' captura qualquer erro relacionado ao banco de dados."
coninuacao = "ou seja, o erro de sintaxe foi capturado e o print do 'cpf repetido' foi acionado."