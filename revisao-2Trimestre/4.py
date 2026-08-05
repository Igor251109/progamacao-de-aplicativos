import _sqlite3

def cadastrar():
    try:
        conexao = _sqlite3.connect('hotelaria.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute('''CREATE TABLE IF NOT EXISTS hoteis (
                       id_hotel INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome_hotel TEXT,
                       cidade_hotel TEXT
                       )
                       ''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS quartos (
                       id_quarto INTEGER PRIMARY KEY AUTOINCREMENT,
                       numero_quarto INTEGER NOT NULL,
                       preco_diaria REAL NOT NULL,
                       id_hotel_escolhido,
                       FOREIGN KEY (id_hotel_escolhido) REFERENCES hoteis (id_hotel)
                       )
                       ''')
        
        print("\n ==== CADASTRAR HOTEL ====")
        nome_hotel = input("qual o nome do hotel?: ")
        cidade_hotel = input("qual o nome da cidade que o hotel está localizado?: ")

        print("\n ==== CADASTRAR QUARTOS ====")
        numero_quarto = int(input("qual o numero do quarto de hotel?: "))
        preco_diaria = float(input("qual o preço da diaria do quarto?: "))
        id_hotel = int(input("qual o ID do hotel do quarto?: "))

        cursor.execute("INSERT INTO hoteis (nome_hotel, cidade_hotel) VALUES (?, ?)", (nome_hotel, cidade_hotel))
        cursor.execute("INSERT INTO quartos (numero_quarto, preco_diaria, id_hotel_escolhido) VALUES (?, ?, ?)", (numero_quarto, preco_diaria, id_hotel))

        conexao.commit()
        conexao.close()

        print("Informações adicionadas com sucesso!")
    
    except ValueError:
        print("-" * 30)
        print("Erro: digite as informações de forma válida.")
        print("-" * 30)
        return
    
    except _sqlite3.IntegrityError:

        print("-" * 30)
        print("ERROR: Erro de integridade.")
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return
    
    except _sqlite3.OperationalError:
        print("-" * 30)
        print("ERROR: erro no banco de dados, verefique o codigo SQL.")
        print("-" * 30)
        return

def ver():
    try:
        conexao = _sqlite3.connect('hotelaria.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM quartos")

        print("\n ==== CADASTROS ====")
        dados = cursor.fetchall()

        for quarto in dados:
            print(quarto)
    
    except _sqlite3.OperationalError:
        print("-" * 30)
        print("ERROR: Erro operacional no Banco de Dados.")
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return

def atualizar():
    try:
        conexao = _sqlite3.connect('hotelaria.db')
        cursor = conexao.cursor()

        ver()

        cursor.execute("SELECT * FROM quartos")
        dados = cursor.fetchall()

        qual_mudar = int(input("qual o ID que deseja alterar?: "))

        if not dados:
            print("não há nenhum cadastro no sistema.")
            return

        print("\n ==== MENU DE ALTERAÇÃO ====")
        numero_quarto = int(input("qual o numero do quarto de hotel?: "))
        preco_diaria = float(input("qual o preço da diaria do quarto?: "))
        id_hotel = int(input("qual o ID do hotel do quarto?: "))

        cursor.execute("UPDATE quartos SET numero_quarto = ?, preco_diaria = ?, id_hotel_escolhido = ?", (numero_quarto, preco_diaria, id_hotel))

        conexao.commit()
        conexao.close()

        print("informações atualizadas com sucesso!")

    except _sqlite3.OperationalError:
        print("-" * 30)
        print("ERROR: erro operacional no banco de dados.")
        print("-" * 30)
        return
    
    except _sqlite3.IntegrityError:
        print("-" * 30)
        print("ERROR: erro de integridade.")
        print("-" * 30)
        return
        
    except ValueError:
        print("-" * 30)
        print("ERROR: digite as informações de maneira válida.")
        print("-" * 30)
        return
    
    except IndexError:
         # Trata erros ao acessar posições inexistentes em listas, tuplas ou strings.

        print("-" * 30)
        print("ERROR: Tentativa de acessar um dado inexistente na tabela/coluna.")
        print("-" * 30)
        return
    
    except KeyboardInterrupt:  
         # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.

        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return

def deletar():
    try:
        conexao = _sqlite3.connect('hotelaria.db')
        cursor = conexao.cursor()

        ver()

        cursor.execute("SELECT * FROM quartos")
        dados = cursor.fetchall()

        if not dados:
            print("não há nenhum cadastro no sitema.")
            return
        
        print("\n ==== DELETAR CADASTRO ==== ")
        qual_mudar = int(input("qual o ID que deseja deletar?: "))

        cursor.execute("DELETE FROM quartos WHERE id_quarto = ?", (qual_mudar, ))

        conexao.commit()
        conexao.close()

        print("Cadastro deletado com sucesso! ")
    
    except _sqlite3.OperationalError:
        print("-" * 30)
        print("ERROR: erro no banco de dados, verefique o codigo SQL.")
        print("-" * 30)
        return

    except ValueError:
        print("-" * 30)
        print("ERROR: digite um número válido.")
        print("-" * 30)
        return
    
    except IndexError:
        print("-" * 30)
        print("ERROR: Tentativa de acessar um dado inexistente na tabela/coluna.")
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
        print("-" * 30)
        print("Operação cancelada pelo usuário, programa encerrado.")
        print("-" * 30)
        return

def menu():
    try:
        while True:
            print("\n ==== MENU DE INTERAÇÃO DO USUÁRIO ==== ")
            print("1. cadastrar")
            print("2. ver")
            print("3. atualizar")
            print("4. deletar")
            print("5. sair")

            opcao = int(input("qual opção vai escolher?: "))

            if opcao == 1: cadastrar()
            elif opcao == 2: ver()
            elif opcao == 3: atualizar()
            elif opcao == 4: deletar()
            elif opcao == 5:
                print("encerrando programa...")
                break
            else:
                print("opção inválida. tente novamente.")
                continue
        
    except ValueError:
            print("-" * 30)
            print("ERROR: digite um número valido.")
            print("-" * 30)
            return

    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
            print("-" * 30)
            print("Operação cancelada pelo usuário, programa encerrado.")
            print("-" * 30)
            return

menu()