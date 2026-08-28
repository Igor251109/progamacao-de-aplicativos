import sqlite3

def conectar():
    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    return conexao, cursor

def criar_escolas():
    conexao = None
    cursor = None 

    try:
        conexao, cursor = conectar()

        cursor.execute('''CREATE TABLE IF NOT EXISTS escolas (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome_escola TEXT NOT NULL,
                       cidade_escola TEXT NOT NULL
                       )
                       ''')
        
        conexao.commit()
    finally:
        conexao.close()

def criar_turmas():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()

        cursor.execute('''CREATE TABLE IF NOT EXISTS turmas (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome_turma TEXT NOT NULL,
                       id_escola INTEGER NOT NULL,
                       FOREIGN KEY (id_escola) REFERENCES escolas(id)
                       )
                       ''')
        
        conexao.commit()
    finally:
        conexao.close()

def criar_alunos():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()

        cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       idade INTEGER NOT NULL,
                       id_turma INTEGER NOT NULL,
                       FOREIGN KEY (id_turma) REFERENCES turmas(id)
                       )
                       ''')
        
        conexao.commit()
    finally:
        conexao.close()