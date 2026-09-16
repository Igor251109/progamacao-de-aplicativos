# Use busca binária para verificar se uma palavra está presente em uma lista de palavras ordenadas alfabeticamente.
import sqlite3

conexao = sqlite3.connect("exercicios.db")
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS nomes_ordenados (
        id_nome INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL
    )
''')

def adicionar(nome):
    cursor.execute(
        '''INSERT INTO nomes_ordenados (nome) VALUES (?)''',
        (nome,)
    )
    conexao.commit()
    print("Deu certo.")


def ver(nome):
    cursor.execute('''
        SELECT nome
        FROM nomes_ordenados
        ORDER BY nome
    ''')

    dados = cursor.fetchall()

    # Transformando os resultados em uma lista
    lista = [linha[0] for linha in dados]

    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == nome:
            print("O nome está na lista!")
            return

        elif lista[meio] < nome:
            inicio = meio + 1

        else:
            fim = meio - 1

    print("O nome não está na lista.")

ver("robson")

conexao.close()