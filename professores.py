import sqlite3
conexao = sqlite3.connect('escola_demostracao.db')
cursor = conexao.cursor()

cursor.execute('''create table if not exists professores (
               id_professor integer primary key autoincrement,
               nome_professor text not null,
               telefone_professor text not null,
               materia_professor text,
               idade_professor integer not null,
               cpf_professor text not null,
               salario_professor text,
               nome_colegio text
               ) ''' )

def registrar_professores():
    print("\n ==== REGISTRAR PROFESSORES ====")
    nome = input("Qual o nome completo do professor? (obrigatório): ")
    telefone = input("Qual o telefone do professor? (obrigatório): ")
    materia = input("Qual a matéria do professor? (opcional): ")
    idade = int(input("Qual a idade do professor?(obrigatório): "))
    cpf = input("qual o CPF do professor? (obrigatório): ")
    salario = input("qual o salário atual do professor? (opcional): ")
    nome_colegio = input("qual o nome do colégio? (obrigatório): ")

    comando_inserir = f'''INSERT into professores (nome_professor, telefone_professor, materia_professor, idade_professor, cpf_professor, salario_professor, nome_colegio)
     values ('{nome}', '{telefone}', '{materia}', {idade}, '{cpf}', '{salario}', '{nome_colegio}') '''
    
    cursor.execute(comando_inserir)
    print("professor registrado com sucesso!")
    conexao.commit()
    conexao.close()
    return

def ver_professores():
    print("\n ==== PROFESSORES REGISTRADOS ==== ")

    professores = cursor.fetchall
    cursor.execute("SELECT * FROM professores")

    for professor in professores:
        print(professor)

def atualizar_professores():
    ver_professores()

    print("\n ==== ATUALIZAR PROFESSORES ====")
    
    id_professor = int(input("qual o ID do professor que deseja atualizar?: "))

    cursor.execute(f"SELECT * FROM professores WHERE id_professor = {id_professor}")

    professor = cursor.fetchone()

    if not professor:
        print("não encontrado.")
        conexao.close()
        return
    
    else:
        nome = input()