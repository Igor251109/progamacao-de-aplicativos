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

        cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
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

        conexao.commit()
        conexao.close()

    except ValueError:
        print("-" * 45)
        print("dados digitados invalidos")
        print("-" * 45)
        return
    except sqlite3.IntegrityError:
        print("-" * 30)
        print("ERROR: Erro de integridade.")
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   
        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return

def ver():
    try:
        conexao = sqlite3.connect('academias.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM alunos")
        dados = cursor.fetchall()

        print("\n ==== ALUNOS CADASTRADOS ====")

        for alunos in dados:
            print(alunos)

    except sqlite3.OperationalError:
        print("-" * 30)
        print("ERROR: Erro operacional no Banco de Dados.")
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   
        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return

def menu():
    try:
        while True:
            print("\n ==== MENU ====")
            print("1. adicionar")
            print("2. ver")
            print("3. sair")

            opcao = int(input("qual opção vai escolher?: "))

            if opcao == 1: cadastrar()
            elif opcao == 2: ver()
            elif opcao == 3:
                print("encerrado.")
                break
            else:
                print("numero inválido! ")
                continue
    except ValueError:
            print("-" * 30)
            print("ERROR: digite um número valido.")
            print("-" * 30)
            

    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
            print("-" * 30)
            print("Operação cancelada pelo usuário, programa encerrado.")
            print("-" * 30)
            return

menu()