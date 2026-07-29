#            import sqlite3 
 
#            def verificar_registros(): 
#                conexao = sqlite3.connect('sistema_escola.db') 
#            	cursor = conexao.cursor() 
     
#                cursor.execute("SELECT * FROM alunos") 
     
            	# Por que o segundo print não mostra absolutamente nada no console? 
#                print("Primeiro print:", cursor.fetchall()) 
#                print("Segundo print:", cursor.fetchall()) 
     
#                conexao.close()

#               RESOLUÇÃO:

import sqlite3 
 
def verificar_registros(): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 

    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL
                   )
                   ''')
     
    cursor.execute("SELECT * FROM alunos") 
    print("Primeiro print:", cursor.fetchall())

    cursor.execute("SELECT * FROM alunos") 
    print("Segundo print:", cursor.fetchall()) 
     
    conexao.close()
verificar_registros()