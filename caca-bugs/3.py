#import sqlite3

#def criar_tabelas():
    #conexao = sqlite3.connect('sistema_escola.db')
    #cursor = conexao.cursor()

    # Este bloco quebra ao rodar pela primeira vez em um banco limpo. por que?
   # cursor.execute('''
#CREATE TABLE IF NOT EXISTS series (
                   #id INTEGER PRIMARY KEY AUTOINCREMENT,
                   #nome_serie TEXT,
                   #id_escola INTEGER,
                   #FOREIGN KEY (id_escola) REFERENCES escolas (id)
                  # )
                  # ''')
    
    #cursor.execute('''
#CREATE TABLE IF NOT EXISTS escolas (
                   #id INTEGER PRIMARY KEY AUTOINCREMENT,
                   #nome TEXT
                   #)
                  # ''')
    
   # conexao.commit()
    #conexao.close()

                # o código da erro por estar na ordem invertida de criação de tabelas. ordem correta:

import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
CREATE TABLE IF NOT EXISTS escolas (
                   #id INTEGER PRIMARY KEY AUTOINCREMENT,
                   #nome TEXT
                   )
                   ''')
    
    cursor.execute('''
CREATE TABLE IF NOT EXISTS series (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome_serie TEXT,
                   id_escola INTEGER,
                   FOREIGN KEY (id_escola) REFERENCES escolas (id)
                   )
                   ''')
    
    conexao.commit()
    conexao.close()