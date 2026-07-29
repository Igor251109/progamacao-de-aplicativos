#            import sqlite3 
 
            # O aluno criou a conexão fora das funções para "facilitar". 
            # Por que isso quebra o sistema quando usamos múltiplos arquivos (módulos)? 
#            conexao = sqlite3.connect('sistema_escola.db') 
#            cursor = conexao.cursor() 
 
#            def inserir_escola(nome): 
#                cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome,)) 
#                conexao.commit()

#                  RESOLUÇÃO:

import sqlite3  
 
def inserir_escola(nome):
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 

    cursor.execute('''CREATE TABLE IF NOT EXISTS escolas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT
                   )
                   ''')

    cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome,)) 
    conexao.commit() 
    print("adicionado")

nome = "igor"

inserir_escola(nome)

#    RESPOSTA:

# Uma conexão global quebra porque ela expira, fecha sozinha ou gera conflitos
# quando diferentes arquivos tentam usá-la ao mesmo tempo,
# enquanto abri-la dentro da função garante que cada comando tenha sua própria conexão nova e segura.