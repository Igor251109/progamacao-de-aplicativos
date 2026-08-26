import sqlite3

def conectar_db():
    conexao = sqlite3.connect('clinica_veterinaria.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    return conexao, cursor


def criar_tabela_franquia():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar_db()

        cursor.execute('''CREATE TABLE IF NOT EXISTS franquias_pet (
                        id_franquia INTEGER PRIMARY KEY AUTOINCREMENT,
                        marca_franquia TEXT NOT NULL,
                        site_franquia TEXT NOT NULL
                        )
                        ''')
        conexao.commit()

    finally:
        conexao.close()

def adicionar_franquias():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar_db()

        print("\n ==== ADICIONAR FRANQUIAS VETERINÁRIAS ==== ")

        marca = input("qual o nome da franquia?: ")
        site = input("qual o nome do site da franquia?: ")

        cursor.execute(" INSERT INTO franquias_pet (marca_franquia, site_franquia) VALUES (?, ?)", (marca, site))

        conexao.commit()

        print("franquia adicionada com sucesso!")

    finally:
        conexao.close()

def ver_franquias():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar_db()

        cursor.execute('''SELECT id_franquia, marca_franquia, site_franquia FROM franquias_pet''')
        franquias = cursor.fetchall()

        print("\n ==== FRANQUIAS REGISTRADAS ====")

        if not franquias:
            print("não há nenhuma franquia registrada.")
        else:
            for franquia in franquias:
                id_franquia, marca, site = franquia

                print(f"id franquia: {id_franquia}")
                print(f"marca: {marca}")
                print(f"site: {site}")
                print("-" * 30)

        conexao.commit()
    
    finally:
        conexao.close()

