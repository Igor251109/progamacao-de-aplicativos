import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor

    # O aluno tenta cadastrar uma série com id_escola = 999 (que não existe).
    # O SQLite aceita o cadastro mesmo assim. O que está faltando ativar?

    try:
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)", (nome_serie, id_escola))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("erro: Escola inexistente!")
    finally:
        conexao.close()