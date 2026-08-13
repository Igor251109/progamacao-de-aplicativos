import sqlite3

def conectar_db():
    conexao = sqlite3.connect('clinica_veterinaria.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    return conexao, cursor

def tratar_erros_funcoes(funcao):
    try:
        funcao()
    
    except ValueError:
        print("-" * 30)
        print("dados inválidos.")
        print("-" * 30)
        return
    except KeyboardInterrupt:
        print("-" * 30)
        print("encerrando programa.")
        print("-" * 30)
        return
    except sqlite3.OperationalError:
        print("-" * 30)
        print("erro operacional no banco de dados.")
        print("-" * 30)
        return
    except sqlite3.IntegrityError:
        print("-" * 30)
        print("erro d intregidade no banco de dados.")
        print("-" * 30)
        return
    except SyntaxError:
        print("-" * 30)
        print("erro de sintaxe.")
        print("-" * 30)
        return
    except IndexError:
        print("-" * 30)
        print("o numero não existe.")
        print("-" * 30)

def criar_tabelas():
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

def adicionar_clinicas():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar_db()

        print("\n ==== ADICIONAR CLINICAS ====")

        bairro = input("qual o bairro da clinica?: ")
        id_franquia = int(input("qual ID da franquia?: "))

        cursor.execute("INSERT INTO clinicas (bairro_clinica, id_franquia_selecionada) VALUES (?, ?)", (bairro, id_franquia))

        conexao.commit()

        print("-" * 30)
        print("clinica adicionada com sucesso!")

    finally:
        conexao.close()

def ver_franquias():
    conexao = None
    cursor = None

    try:

        conexao, cursor = conectar_db()

        print("\n ==== VER FRANQUIAS REGISTRADAS ====")

        cursor.execute('''SELECT clinicas.id_clinica, clinicas.bairro_clinica, franquias_pet.marca_franquia, franquias_pet.site_franquia
                       FROM clinicas INNER JOIN franquias_pet ON clinicas.id_franquia_selecionada = franquias_pet.id_franquia'''
        )

        clinicas = cursor.fetchall()

        print("\n ==== CLINICAS REGISTRADAS ====")

        if not clinicas:
            print("não há nenhuma clinica registrada.")
            return
        
        for clinica in clinicas:
            id_clinica, bairro_clinica, marca_franquia, site = clinica

            print(f"id clinica: {id_clinica},")
            print(f"marca: {marca_franquia},")
            print(f"site: {site},")
            print(f"bairro: {bairro_clinica}")
            print("-" * 30)
    
    finally:
        conexao.close()
    
def atualizar():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar_db()

        ver_franquias()

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

        print("\n ==== DELETAR CADASTROS ==== ")

        qual_deletar = int(input("qual ID da clinica que deseja deletar?: "))

        cursor.execute("SELECT * FROM clinicas")
        dados = cursor.fetchall()

        if not dados:
            print("não há nenhum registro.")
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

def menu():
    while True:
        print("\n ==== MENU DE INTERAÇÃO ====")
        print("1. ADICIONAR FRANQUIAS E CLINICAS")
        print("2. VER REGISTROS")
        print("3. ATUALIZAR CLINICAS")
        print("4. DELETAR CLINICAS")
        print("5. SAIR")

        opcao = int(input("qual opção vai escolher?: "))

        if opcao == 1:
            tratar_erros_funcoes(adicionar_franquias)
            tratar_erros_funcoes(adicionar_clinicas)
        elif opcao == 2:
            tratar_erros_funcoes(ver_franquias)
        elif opcao == 3:
            tratar_erros_funcoes(atualizar)
        elif opcao == 4:
            tratar_erros_funcoes(deletar)
        elif opcao == 5:
            print("-" * 30)
            print("encerrando sistema...")
            print("-" * 30)
            break
        else:
            print("-" * 30)
            print("opção invalida. tente novamente.")
            print("-" * 30)
            continue

tratar_erros_funcoes(criar_tabelas)
tratar_erros_funcoes(menu)