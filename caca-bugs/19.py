#            import sqlite3 
 
#            def buscar_dados_dinamicos(nome_tabela, id_registro): 
#                conexao = sqlite3.connect('sistema_escola.db') 
#            	cursor = conexao.cursor() 
     
            	# O SQLite joga um erro de sintaxe operacional indicando que não aceita o caractere '?'. 
            	# Não podemos parametrizar nomes de tabelas? Como resolver mantendo a segurança? 
#                cursor.execute("SELECT * FROM ? WHERE id = ?", (nome_tabela, id_registro)) 
     
#            	print(cursor.fetchone()) 
#                conexao.close()

resposta = "não podemos usar colunas ou tabelas como parâmetros."

#        CORREÇÃO:
import sqlite3 
 
def buscar_dados_dinamicos(): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome_tabela TEXT,
                   id_registro INTEGER
                   )
                   ''') 

    idx = 1
      
    cursor.execute("SELECT * FROM alunos WHERE id = ?", (idx,)) 
     
    print(cursor.fetchone()) 
    print("encontrado")
    conexao.close()

buscar_dados_dinamicos()