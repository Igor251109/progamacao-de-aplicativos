# Contexto: A secretaria da escola aprovou o banco de dados que o professor criou.
# Agora, sua missão como programador é criar um sistema interativo que converse com o usuário através do terminal,
# colete as informações de um novo aluno e salve tudo dentro do arquivo escola_demonstracao.db
# usando o comando INSERT com F-Strings.

import sqlite3
conexao = sqlite3.connect('escola_demostracao.db')
cursor = conexao.cursor()

cursor.execute ('''create table if not exists alunos (
    id_aluno integer primary key autoincrement,
    nome_aluno text not null,
    telefone_aluno text not null,
    turma_aluno text,
    idade_aluno integer not null,
    cpf_aluno text not null
)''')

nome = input("qual o nome completo do aluno?: ")
telefone = input("qual o telefone do aluno?: ")
turma = input("qual a turma do aluno?: (opcional)")
idade = int(input("qual a idade do aluno?: "))
cpf = input("qual o CPF do aluno?: ")

comando_inserir = f'''insert into alunos (nome_aluno, telefone_aluno, turma_aluno, idade_aluno, cpf_aluno)
values ('{nome}', '{telefone}', '{turma}', '{idade}', '{cpf}')'''

cursor.execute(comando_inserir)
conexao.commit()

cursor.execute("SELECT * FROM alunos")
dados = cursor.fetchall()

for aluno in dados:
    print(aluno)
    
conexao.close()

print("aluno registrado com sucesso!")