import sqlite3

def cadastrar():
    try:
        conexao = sqlite3.connect('cinemas.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute('''CREATE TABLE IF NOT EXISTS cinemas (
                    id_cinema INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_cinema TEXT NOT NULL,
                    cidade_cinema TEXT NOT NULL
                    )
                    ''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS salas (
                    id_sala INTEGER PRIMARY KEY AUTOINCREMENT,
                    numero_sala INTEGER NOT NULL,
                    capacidade INTEGER NOT NULL,
                    id_cinema_escolhido INTEGER,
                    FOREIGN KEY (id_cinema_escolhido) REFERENCES cinemas (id_cinema)
                    )
                    ''')
        
        nome_cinema = input("qual o nome do cinema? (obrigatório): ")
        cidade_cinema = input("qual a cidade que o cinema está localizado? (obrigatório): ")
        print("-" * 45)
        numero_sala = int(input("qual o numero da sala de cinema? (obrigatório): "))
        capacidade_sala = int(input("qual a capacidade de pessoas da sala? (obrigatório): "))
        id_cinema = int(input("qual o ID desse cinema? (obrigatório): "))

        cursor.execute(f"INSERT INTO cinemas (nome_cinema, cidade_cinema) VALUES ('{nome_cinema}', '{cidade_cinema}')")

        cursor.execute(f"INSERT INTO salas (numero_sala, capacidade, id_cinema_escolhido) VALUES ({numero_sala}, {capacidade_sala}, {id_cinema})")

        print("informações adicionadas! ")

        conexao.commit()
        conexao.close()
    
    except ValueError as e:
        print(f"digite as informaçõs de forma valida. {e}")
        return
    except KeyboardInterrupt as e:
        print(f"programa encerrado pelo usuário, voltando a tela inicial. {e}")
        return
    except sqlite3.IntegrityError as e:
        print(f"erro de integridade no banco de dados. {e}")
        return
    except sqlite3.OperationalError as e:
        print(f"erro operacional no banco de dados. {e}")
        return

def ver():
    try:
        conexao = sqlite3.connect('cinemas.db')
        cursor = conexao.cursor()

        print("\n ==== VER ====")

        cursor.execute("SELECT * FROM salas")
        dados = cursor.fetchall()

        for sala in dados:
            print(f"salas de cinema: {sala}")

    except sqlite3.OperationalError:
        print("-" * 30)
        print("ERROR: Erro operacional no Banco de Dados.")
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return

def menu():
    try:
        while True:
            print("\n ==== MENU INTERAÇÃO ====")
            print("1. adicionar")
            print("2. ver salas")
            print("3. sair")

            op = int(input("qual opção vai escolher: "))

            if op == 1:
                cadastrar()
            elif op == 2:
                ver()
            elif op == 3:
                print("programa encerrado.")
                break
            else:
                print("tentativa invalida, tente novamente.")
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