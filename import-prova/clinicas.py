import sqlite3
from franquias import ver_franquias

def conectar_db():
    conexao = sqlite3.connect('clinica_veterinaria.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    return conexao, cursor

def criar_tabela_clinica():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar_db()

        cursor.execute('''CREATE TABLE IF NOT EXISTS clinicas (
                        id_clinica INTEGER PRIMARY KEY AUTOINCREMENT,
                        bairro_clinica TEXT,
                        id_franquia_selecionada INTEGER ,
                        FOREIGN KEY (id_franquia_selecionada) REFERENCES franquias_pet (id_franquia)
                        )
                        ''')
        
        conexao.commit()
    finally:
        conexao.close()

def adicionar_clinicas():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar_db()
        ver_franquias()

        print("\n ==== ADICIONAR CLINICAS ====")
        print("\n == ATENÇÃO!: Só será possivel adicionar clinicas que usem o ID de uma franquia existente.")

        bairro = input("qual o bairro da clinica?: ")
        id_franquia = int(input("qual ID da franquia?: "))

        cursor.execute("SELECT id_franquia FROM franquias_pet WHERE id_franquia = ?", (id_franquia, ))
        franquia = cursor.fetchone()

        if franquia is None:
            print("insira um ID valido de uma franquia. operação cancelada")
            return

        cursor.execute("INSERT INTO clinicas (bairro_clinica, id_franquia_selecionada) VALUES (?, ?)", (bairro, id_franquia))

        conexao.commit()

        print("-" * 30)
        print("clinica adicionada com sucesso!")

    finally:
        conexao.close()

def ver_clinicas():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar_db()

        cursor.execute("""
            SELECT clinicas.id_clinica,
                   clinicas.bairro_clinica,
                   franquias_pet.marca_franquia
            FROM clinicas
            LEFT JOIN franquias_pet
            ON clinicas.id_franquia_selecionada = franquias_pet.id_franquia
        """)

        clinicas = cursor.fetchall()

        print("\n ==== CLÍNICAS REGISTRADAS ====")

        if not clinicas:
            print("não há nenhuma clínica registrada.")
        else:
            for clinica in clinicas:
                id_clinica, bairro, marca = clinica

                print(f"id clínica: {id_clinica}")
                print(f"bairro: {bairro}")
                print(f"franquia: {marca}")
                print("-" * 30)

    finally:
        if conexao:
            conexao.close()

def atualizar():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar_db()

        ver_franquias()
        ver_clinicas()

        cursor.execute("SELECT * FROM clinicas")
        dados = cursor.fetchall()

        print("\n ==== ATUALIZAR CADASTROS ====")

        qual_mudar = int(input("qual ID da clinica que deseja atualizar?: "))

        if not dados:
            print("não há nenhum registro.")
            return
        
        bairro = input("qual o bairro da clinica?: ")
        id_franquia = int(input("qual ID da franquia?: "))
        print("-" * 30)

        cursor.execute("SELECT id_clinica FROM clinicas WHERE id_clinica = ?", (qual_mudar,))

        clinica = cursor.fetchone()

        if clinica is None:
            print("ID de clínica inválido.")
            return


        certeza = input("tem certeza que deseja alterar esse cadastro? essa ação será irreverssivel. (digite 'sim' para proseguir): ")

        if certeza == "sim" or certeza == "s":
            cursor.execute("UPDATE clinicas SET bairro_clinica = ?, id_franquia_selecionada = ? WHERE id_clinica = ?", (bairro, id_franquia, qual_mudar))

            conexao.commit()

            print("-" * 30)
            print("informações alteradas com sucesso!")
            print("-" * 30)
        
        else:
            print("-" * 30)
            print("operação cancelada.")
            return

    finally:
        conexao.close()

def deletar():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar_db()

        ver_franquias()
        ver_clinicas()

        print("\n ==== DELETAR CADASTROS ==== ")

        qual_deletar = int(input("qual ID da clinica que deseja deletar?: "))

        cursor.execute("SELECT * FROM clinicas")
        dados = cursor.fetchall()

        if not dados:
            print("não há nenhum registro.")
            print("-" * 30)
            return
        
        cursor.execute("SELECT id_clinica FROM clinicas WHERE id_clinica = ?", (qual_deletar,))

        clinica = cursor.fetchone()

        if clinica is None:
            print("ID de clínica inválido. Operação cancelada.")
            return

        certeza = input("tem certeza que deseja deletar esse cadastro? Essa ação será irreverssivel. (digite 'sim' para prosseguir): ")

        if certeza == "sim" or certeza == "s":
            cursor.execute("DELETE FROM clinicas WHERE id_clinica = ?", (qual_deletar,))

            conexao.commit()

            print("-" * 30)
            print("clinica deletada com sucesso!")
        
        else:
            print("-" * 30)
            print("operação cancelada.")
            return

    finally:
        conexao.close()