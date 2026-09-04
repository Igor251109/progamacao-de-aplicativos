import sqlite3

def conectar():     # conectar ao banco de dados.
    conexao = sqlite3.connect("reserva_laboratorios.db")
    cursor = conexao.cursor()

    return conexao, cursor

def laboratorios():   # criar a tabela dos laboratorios.
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()

        cursor.execute('''CREATE TABLE IF NOT EXISTS laboratorios (
                       id_laboratorio INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome_laboratorio TEXT NOT NULL,
                       datas TEXT NOT NULL,
                       horario TEXT NOT NULL,
                       nome_solicitante TEXT NOT NULL
                       )
                       ''')
        conexao.commit()
    finally:
        if conexao:
            conexao.close()
