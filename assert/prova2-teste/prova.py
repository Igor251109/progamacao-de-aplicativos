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
        return

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

tratar_erros_funcoes(criar_tabelas)

def adicionar_franquias(marca, site):
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar_db()

        print("\n ==== ADICIONAR FRANQUIAS VETERINÁRIAS ==== ")

        cursor.execute(" INSERT INTO franquias_pet (marca_franquia, site_franquia) VALUES (?, ?)", (marca, site))

        conexao.commit()

        print("franquia adicionada com sucesso!")

        return marca, site

    finally:
        conexao.close()

assert adicionar_franquias("sesi", "sesi.com") == ("sesi", "sesi.com")
print("certo")

def adicionar_clinicas(bairro, id_franquia):
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar_db()

        print("\n ==== ADICIONAR CLINICAS ====")
        print("\n == ATENÇÃO!: Só será possivel adicionar clinicas que usem o ID de uma franquia existente.")

        cursor.execute("SELECT id_franquia FROM franquias_pet WHERE id_franquia = ?", (id_franquia, ))
        franquia = cursor.fetchone()

        if franquia is None:
            print("insira um ID valido de uma franquia. operação cancelada")
            return

        cursor.execute("INSERT INTO clinicas (bairro_clinica, id_franquia_selecionada) VALUES (?, ?)", (bairro, id_franquia))

        conexao.commit()

        print("-" * 30)
        print("clinica adicionada com sucesso!")

        return bairro, id_franquia

    finally:
        conexao.close()

assert adicionar_clinicas("santos dumont", 1) == ("santos dumont", 1)
print("certo")

def ver_franquias_e_clinicas():
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
    
def atualizar(qual_mudar, bairro, id_franquia):
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar_db()

        cursor.execute("SELECT * FROM clinicas")
        dados = cursor.fetchall()

        print("\n ==== ATUALIZAR CADASTROS ====")


        if not dados:
            print("não há nenhum registro.")
            return

        cursor.execute("SELECT id_franquia FROM franquias_pet WHERE id_franquia = ?", (id_franquia, ))
        franquia = cursor.fetchone()

        if franquia is None:
            print("insira um ID valido de uma franquia. operação cancelada")
            return

        cursor.execute("UPDATE clinicas SET bairro_clinica = ?, id_franquia_selecionada = ? WHERE id_clinica = ?", (bairro, id_franquia, qual_mudar))

        conexao.commit()

        print("-" * 30)
        print("informações alteradas com sucesso!")
        print("-" * 30)

        return qual_mudar, bairro, id_franquia

    finally:
        conexao.close()

assert atualizar(1, "ouro branco", 1) == (1, "ouro branco", 1)
print("certo")

def deletar(qual_deletar):
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar_db()

        ver_franquias_e_clinicas()

        print("\n ==== DELETAR CADASTROS ==== ")

        cursor.execute("SELECT * FROM clinicas")
        dados = cursor.fetchall()

        if not dados:
            print("não há nenhum registro.")
            print("-" * 30)
            return
        
        cursor.execute("SELECT id_franquia FROM franquias_pet WHERE id_franquia = ?", (qual_deletar, ))
        franquia = cursor.fetchone()

        if franquia is None:
            print("insira um ID valido de uma franquia. operação cancelada")
            return

        cursor.execute("DELETE FROM clinicas WHERE id_clinica = ?", (qual_deletar,))

        conexao.commit()

        print("-" * 30)
        print("clinica deletada com sucesso!")
        
        return qual_deletar

    finally:
        conexao.close()

assert deletar(1) == 1
print("certo")

def menu():
    while True:
        print("\n ==== MENU DE INTERAÇÃO ====")
        print("1. ADICIONAR FRANQUIAS")
        print("2. ADICIONAR CLÍNICAS")
        print("3. VER REGISTROS")
        print("4. ATUALIZAR CLINICAS")
        print("5. DELETAR CLINICAS")
        print("6. SAIR")

        opcao = int(input("qual opção vai escolher?: "))

        if opcao == 1:
            tratar_erros_funcoes(adicionar_franquias)
            quer_adicionar = input("deseja adicionar uma clínica? (digite sim ou não): ")
            if quer_adicionar == "sim":
                tratar_erros_funcoes(adicionar_clinicas)

        elif opcao == 2:
            tratar_erros_funcoes(adicionar_clinicas)

        elif opcao == 3:
            tratar_erros_funcoes(ver_franquias_e_clinicas)

        elif opcao == 4:
            tratar_erros_funcoes(atualizar)

        elif opcao == 5:
            tratar_erros_funcoes(deletar)

        elif opcao == 6:
            print("-" * 30)
            print("encerrando sistema...")
            print("-" * 30)
            break

        else:
            print("-" * 30)
            print("opção invalida. tente novamente.")
            print("-" * 30)
            continue

tratar_erros_funcoes(menu)