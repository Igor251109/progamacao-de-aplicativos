#            import sqlite3 
 
#            def listar_alunos_e_turmas(): 
#                conexao = sqlite3.connect('sistema_escola.db') 
#                cursor = conexao.cursor() 
     
	            # O relatório roda, mas repete os dados erroneamente em formato de matriz cruzada 
	            # porque falta definir a regra de colagem (vínculo). Conserte o comando SQL: 
#                cursor.execute("SELECT alunos.nome, turmas.nome_turma FROM alunos INNER JOIN turmas") 
     
#                for linha in cursor.fetchall(): 
#                    print(f"Aluno: {linha[0]} | Turma: {linha[1]}") 
#                conexao.close()

resposta = "falta o comando 'ON' no código. Sem o 'ON', os alunos seram adicionados em TODAS AS TURMAS, virando uma bagunça."

import sqlite3 
 
def listar_alunos_e_turmas(): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 

    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome_alunos TEXT,
                   turma_id INTEGER
                   )
                   ''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS turmas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome_turmas TEXT
                   )
                   ''')
    
    cursor.execute("INSERT INTO alunos (id, nome_alunos, turma_id) VALUES (1, 'igor', 1)")
    cursor.execute("INSERT INTO turmas (id, nome_turmas) VALUES (1, '1 ano')")
      
    cursor.execute("SELECT alunos.nome_alunos, turmas.nome_turmas FROM alunos INNER JOIN turmas ON alunos.turma_id = turmas.id") 
     
    for linha in cursor.fetchall(): 
        print(f"Aluno: {linha[0]} | Turma: {linha[1]}")

    conexao.commit()
    conexao.close()
    print("olá mundo!") 
listar_alunos_e_turmas()