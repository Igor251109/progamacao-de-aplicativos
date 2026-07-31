import sqlite3
conexao = sqlite3.connect('escola_demostracao.db')
cursor = conexao.cursor()

cursor.execute(
    '''ALTER TABLE professores ADD COLUMN
    endereco TEXT'''
)

conexao.commit()