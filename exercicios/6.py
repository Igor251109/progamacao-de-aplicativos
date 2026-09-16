# Implemente busca binária em um vetor ordenado de números inteiros. A função deve retornar o índice do elemento ou -1 caso não exista.

import sqlite3

conexao = sqlite3.connect("exercicios.db")
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS numeros_ordenados (
               id_numero INTEGER PRIMARY KEY AUTOINCREMENT,
               numero INTEGER UNIQUE NOT NULL
               )
               ''')

def adicionar(numero):
    cursor.execute('''INSERT INTO numeros_ordenados (numero) VALUES (?)''', (numero, ))
    conexao.commit()
    print("deu certo.")

def ver():
    cursor.execute('''SELECT id_numero, numero FROM numeros_ordenados ORDER BY numero''')
    resultados = cursor.fetchall()
    for id_numero, numero in resultados:
        print(f'ID: {id_numero} | Número: {numero}')


ver()

conexao.close()