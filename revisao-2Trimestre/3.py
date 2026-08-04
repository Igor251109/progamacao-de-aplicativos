import sqlite3

def cadastrar():
    try:
        conexao = sqlite3.connect('academias.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute('''CREATE TABLE IF NOT EXISTS academias (
                    id_academia INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_unidade TEXT NOT NULL,
                    bairro_unidade TEXT NOT NULL
                    )
                    ''')

        cursor.execute('''CREATE TABLE IF NOT EXITS alunos (
                    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_aluno TEXT NOT NULL,
                    mensalidade_aluno REAL NOT NULL,
                    id_academia_escolhida INTEGER,
                    FOREIGN KEY (id_academia_escolhida) REFERENCES academias (id_academia)
                    )
                    ''')
        
        print("\n ==== CADASTRAR ACADEMIA ==== ")
        nome_unidade = input("qual o nome da academia?: ")
        bairro = input("qual o bairro da unidade?: ")

        print("\n ==== CADASTRAR ALUNO ==== ")
        nome_aluno = input("qual o nome do aluno?: ")
        mensalidade_do_aluno = float(input("qual o valorda mensalidade do aluno?: "))
        id_academia = int(input("qual o ID da academia de cadastro do aluno?: "))

        cursor.execute("INSERT INTO academias (nome_unidade, bairro_unidade) VALUES (?, ?)", (nome_unidade, bairro))
        cursor.execute("INSERT INTO alunos (nome_aluno, mensalidade_aluno, id_academia_escolhida) VALUES (?, ?, ?)", (nome_aluno, mensalidade_do_aluno, id_academia))

    except ValueError:
        print("dados digitados invalidos")