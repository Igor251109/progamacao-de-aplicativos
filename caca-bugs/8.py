#        import sqlite3 
 
#        def cadastrar_professor(nome, cpf): 
#            conexao = sqlite3.connect('sistema_escola.db') 
#	        cursor = conexao.cursor() 
     
#	        # O sistema aceita cadastrar dois professores com o mesmo CPF. 
#	        # Como restringir isso direto na estrutura da tabela abaixo? 
 #           cursor.execute(''' 
#    	        CREATE TABLE IF NOT EXISTS professores ( 
#        	        id INTEGER PRIMARY KEY AUTOINCREMENT, 
#        	        nome TEXT, 
#                    cpf TEXT 
#                ) 
#	        ''') 

# RESPOSTA: falta o "UNIQUE" no campo "cpf" na criação da tabela.

import sqlite3 
 
def cadastrar_professor(nome, cpf): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
    cursor.execute(''' 
    	CREATE TABLE IF NOT EXISTS professores ( 
        	id INTEGER PRIMARY KEY AUTOINCREMENT, 
        	nome TEXT, 
            cpf TEXT UNIQUE
        ) 
	''') 
