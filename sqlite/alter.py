import sqlite3
conexao = sqlite3.connect('escola_demostracao.db')
cursor = conexao.cursor()

cursor.execute("ALTER TABLE alunos ADD COLUMN endereco TEXT")

conexao.commit()