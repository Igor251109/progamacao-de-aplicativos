import sqlite3

def criar_banco():
    try:
        conexao = sqlite3.connect('hotelaria.db')
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
        
        conexao.commit()

    except sqlite3.IntegrityError as e:

        print("-" * 30)
        print("ERROR: Erro de integridade.", e)
        print("-" * 30)
        return
    
    except sqlite3.OperationalError as e:
        print("-" * 30)
        print("ERROR: erro no banco de dados, verefique o codigo SQL.", e)
        print("-" * 30)
        return
    
    finally:
        conexao.close()

def cadastrar():
    try:
        conexao = sqlite3.connect('hotelaria.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        
        print("\n ==== CADASTRAR HOTEL ====")
        print("-" * 30)
        nome_hotel = input("qual o nome do hotel?: ")
        print("-" * 30)
        cidade_hotel = input("qual o nome da cidade que o hotel está localizado?: ")
        print("-" * 30)

        print("\n ==== CADASTRAR QUARTOS ====")
        print("-" * 30)
        numero_quarto = int(input("qual o numero do quarto de hotel?: "))
        print("-" * 30)
        preco_diaria = float(input("qual o preço da diaria do quarto?: "))
        print("-" * 30)
        id_hotel = int(input("qual o ID do hotel do quarto?: "))

        cursor.execute("INSERT INTO hoteis (nome_hotel, cidade_hotel) VALUES (?, ?)", (nome_hotel, cidade_hotel))
        cursor.execute("INSERT INTO quartos (numero_quarto, preco_diaria, id_hotel_escolhido) VALUES (?, ?, ?)", (numero_quarto, preco_diaria, id_hotel))

        conexao.commit()

        print("-" * 30)
        print("Informações adicionadas com sucesso!")
        print("-" * 30)
    
    except ValueError as e:
        print("-" * 30)
        print("Erro: digite as informações de forma válida.", e)
        print("-" * 30)
        return
    
    except sqlite3.IntegrityError as e:
        print("-" * 30)
        print("ERROR: Erro de integridade.", e)
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return
    
    except sqlite3.OperationalError as e:
        print("-" * 30)
        print("ERROR: erro no banco de dados, verefique o codigo SQL.", e)
        print("-" * 30)
        return
    
    finally:
        conexao.close()

def ver():
    try:
        conexao = sqlite3.connect('hotelaria.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM quartos")
        dados = cursor.fetchall()

        print("\n ==== CADASTROS ====")
        for quarto in dados:
            print(quarto)
    
    except sqlite3.OperationalError as e:
        print("-" * 30)
        print("ERROR: Erro operacional no Banco de Dados.", e)
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return

def atualizar():
    try:
        conexao = sqlite3.connect('hotelaria.db')
        cursor = conexao.cursor()

        ver()

        cursor.execute("SELECT * FROM quartos")
        dados = cursor.fetchall()

        qual_mudar = int(input("qual o ID que deseja alterar?: "))

        if not dados:
            print("-" * 30)
            print("não há nenhum cadastro no sistema.")
            print("-" * 30)
            return

        print("\n ==== MENU DE ALTERAÇÃO ====")
        numero_quarto = int(input("qual o numero do quarto de hotel?: "))
        print("-" * 30)
        preco_diaria = float(input("qual o preço da diaria do quarto?: "))
        print("-" * 30)
        id_hotel = int(input("qual o ID do hotel do quarto?: "))

        cursor.execute("UPDATE quartos SET numero_quarto = ?, preco_diaria = ?, id_hotel_escolhido = ? WHERE id_quarto = ?", (numero_quarto, preco_diaria, id_hotel, qual_mudar))

        conexao.commit()

        print("-" * 30)
        print("informações atualizadas com sucesso!")
        print("-" * 30)

    except sqlite3.OperationalError as e:
        print("-" * 30)
        print("ERROR: erro operacional no banco de dados.", e)
        print("-" * 30)
        return
    
    except sqlite3.IntegrityError as e:
        print("-" * 30)
        print("ERROR: erro de integridade.", e)
        print("-" * 30)
        return
        
    except ValueError as e:
        print("-" * 30)
        print("ERROR: digite as informações de maneira válida.", e)
        print("-" * 30)
        return
    
    except IndexError as e:
         # Trata erros ao acessar posições inexistentes em listas, tuplas ou strings.
        print("-" * 30)
        print("ERROR: Tentativa de acessar um dado inexistente na tabela/coluna.", e)
        print("-" * 30)
        return
    
    except KeyboardInterrupt:  
         # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return
    
    finally:
        conexao.close()

def deletar():
    try:
        conexao = sqlite3.connect('hotelaria.db')
        cursor = conexao.cursor()

        ver()

        cursor.execute("SELECT * FROM quartos")
        dados = cursor.fetchall()

        if not dados:
            print("-" * 30)
            print("não há nenhum cadastro no sitema.")
            print("-" * 30)
            return
        
        print("\n ==== DELETAR CADASTRO ==== ")
        qual_mudar = int(input("qual o ID que deseja deletar?: "))
        print("-" * 30)

        cursor.execute("DELETE FROM quartos WHERE id_quarto = ?", (qual_mudar, ))

        conexao.commit()

        print("Cadastro deletado com sucesso! ")
        print("-" * 30)
    
    except sqlite3.OperationalError as e:
        print("-" * 30)
        print("ERROR: erro no banco de dados, verefique o codigo SQL.", e)
        print("-" * 30)
        return

    except ValueError as e:
        print("-" * 30)
        print("ERROR: digite um número válido.", e)
        print("-" * 30)
        return
    
    except IndexError as e:
        print("-" * 30)
        print("ERROR: Tentativa de acessar um dado inexistente na tabela/coluna.", e)
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
        print("-" * 30)
        print("Operação cancelada pelo usuário, programa encerrado.")
        print("-" * 30)
        return
    
    finally:
        conexao.close()

def menu():
    try:
        while True:
            print("\n ==== MENU DE INTERAÇÃO DO USUÁRIO ==== ")
            print("1. cadastrar")
            print("2. ver")
            print("3. atualizar")
            print("4. deletar")
            print("5. sair")

            print("-" * 30)
            opcao = int(input("qual opção vai escolher?: "))
            print("-" * 30)

            if opcao == 1: cadastrar()
            elif opcao == 2: ver()
            elif opcao == 3: atualizar()
            elif opcao == 4: deletar()
            elif opcao == 5:
                print("-" * 30)
                print("encerrando programa...")
                print("-" * 30)
                break
            else:
                print("-" * 30)
                print("opção inválida. tente novamente.")
                print("-" * 30)
                continue
        
    except ValueError as e:
            print("-" * 30)
            print("ERROR: digite um número valido.", e)
            print("-" * 30)
            return

    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
            print("-" * 30)
            print("Operação cancelada pelo usuário, programa encerrado.")
            print("-" * 30)
            return

criar_banco()
menu()