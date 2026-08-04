import sqlite3

def cadastrar():
    try:
        conexao = sqlite3.connect('hospital.db')
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute('''CREATE TABLE IF NOT EXISTS hospitais (
                    id_hospitais INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_hospitais TEXT NOT NULL,
                    cidade_hospitais TEXT NOT NULL
                    )
                    ''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS medicos (
                    id_medicos INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_medicos TEXT NOT NULL,
                    crm TEXT,
                    id_hospital INTEGER NOT NULL,
                    FOREIGN KEY (id_hospital) REFERENCES hospitais (id_hospitais)
                    )
                    ''')
        
        print("\n ==== CADASTRAR ====")

        nome_hospital = input("qual o nome do hospital? (obrigatório): ")
        cidade_hospital = input("qual o nome da cidade? (obrigatório): ")
        nome_filho = input("qual o nome do filho? (obrigatório): ")
        crm = input("qual o CRM?: ")
        id_hospital = int(input("qual o ID do hospital do nascimento? (obrigatório): "))

        cursor.execute(f"INSERT INTO hospitais (nome_hospitais, cidade_hospitais) VALUES ('{nome_hospital}', '{cidade_hospital}')")

        cursor.execute(f"INSERT INTO medicos (nome_medicos, crm, id_hospital) VALUES ('{nome_filho}', '{crm}', {id_hospital})")

        print("-" * 45)
        print("informações adicionadas com sucesso!")
        print("-" * 45)

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
    
cadastrar()