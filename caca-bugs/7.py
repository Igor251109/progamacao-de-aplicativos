import sqlite3 
 
def cadastrar_turma(nome, id_serie, id_prof):
    try: 
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 
        cursor.execute("PRAGMA foreign_keys = ON;") 
        
        # Se o id_prof não existir, ocorre um IntegrityError. 
        # Se o erro acontecer, o que ocorre com a linha conexao.close()? 
        cursor.execute("INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)", (nome, id_serie, id_prof)) 
        conexao.commit()

    except sqlite3.IntegrityError:
        print("erro no banco de dados.")
        return
    finally:
        conexao.close()


#           import sqlite3 
#            
#            def cadastrar_turma(nome, id_serie, id_prof): 
#                conexao = sqlite3.connect('sistema_escola.db') 
#                cursor = conexao.cursor() 
#                cursor.execute("PRAGMA foreign_keys = ON;") 
#                
#                # Se o id_prof não existir, ocorre um IntegrityError. 
#                # Se o erro acontecer, o que ocorre com a linha conexao.close()? 
#                cursor.execute("INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)", (nome, id_serie, id_prof)) 
#                conexao.commit() 
#                conexao.close()

# RESPOSTA: o codigo não está com tratamento de erros. o banco de dados poderia ficar aberto e acontecer vazamentos.