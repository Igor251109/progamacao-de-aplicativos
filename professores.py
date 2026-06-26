import sqlite3
conexao = sqlite3.connect('escola_demostracao.db')
cursor = conexao.cursor()

# Criar uma tabela "profesores" no banco de dados
cursor.execute('''CREATE TABLE IF NOT EXISTS professores (
               id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
               nome_professor TEXT NOT NULL,
               telefone_professor TEXT NOT NULL,
               materia_professor TEXT,
               idade_professor INTEGER NOT NULL,
               cpf_professor TEXT NOT NULL,
               salario_professor REAL NOT NULL,
               nome_colegio TEXT
               ) ''' )

def registrar_professores():    # registrar professores no banco de dados
    print("\n ==== REGISTRAR PROFESSORES ====")
    
    try:
        nome = input("Qual o nome completo do professor? (obrigatório): ")
        telefone = input("Qual o telefone do professor? (obrigatório): ")
        materia = input("Qual a matéria do professor? (opcional): ")
        idade = int(input("Qual a idade do professor?(obrigatório): "))
        cpf = input("qual o CPF do professor? (obrigatório): ")
        salario = float(input("qual o salário atual do professor? (obrigatório): "))
        nome_colegio = input("qual o nome do colégio? (obrigatório): ")

        comando_inserir = f'''INSERT into professores (nome_professor, telefone_professor, materia_professor, idade_professor, cpf_professor, salario_professor, nome_colegio)
        values ('{nome}', '{telefone}', '{materia}', {idade}, '{cpf}', {salario}, '{nome_colegio}') '''
        
        cursor.execute(comando_inserir)

        print("-" * 30)
        print("professor registrado com sucesso!")
        print("-" * 30)

        conexao.commit()

    except ValueError:
        print("-" * 30)
        print("ERROR: digite as informações de forma válida.")
        print("-" * 30)
        return
    
    except sqlite3.IntegrityError:
        print("-" * 30)
        print("ERROR: Campo obrigatório não preenchido / Dados unicos já existentes")
        print("-" * 30)
        return
    
    except sqlite3.OperationalError:
        print("-" * 30)
        print("ERROR: erro no banco de dados (verefique se esta aberto).")
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return

def ver_professores():
    try:
        cursor.execute("SELECT * FROM professores")
        professores = cursor.fetchall()

        if not professores:
            print("não tem nenhum professor no banco de dados.")
            return

        print("\n ==== PROFESSORES REGISTRADOS ==== ")

        for professor in professores:
            print(professor)
    
    except sqlite3.OperationalError:
        print("-" * 30)
        print("ERROR: erro no banco de dados (verefique se esta aberto).")
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return

def atualizar_professores():    # Atualizar professores já registrados no banco de dados.
    try:
        ver_professores()

        print("\n ==== ATUALIZAR PROFESSORES ====")
        
        id_professor = int(input("qual o ID do professor que deseja atualizar?: "))

        cursor.execute(f"SELECT * FROM professores WHERE id_professor = {id_professor}")

        professor = cursor.fetchone()

        if not professor:
            print("não encontrado.")
            return
        
        else:
            nome = input("Qual o nome completo do professor? (obrigatório): ")
            telefone = input("Qual o telefone do professor? (obrigatório): ")
            materia = input("Qual a matéria do professor? (opcional): ")
            idade = int(input("Qual a idade do professor?(obrigatório): "))
            cpf = input("qual o CPF do professor? (obrigatório): ")
            salario = float(input("qual o salário atual do professor? (obrigatório): "))
            nome_colegio = input("qual o nome do colégio? (obrigatório): ")

            cursor.execute(
                f"UPDATE professores SET nome_professor = '{nome}', telefone_professor = '{telefone}', materia_professor = '{materia}', idade_professor = {idade}, cpf_professor = '{cpf}', salario_professor = {salario}, nome_colegio = '{nome_colegio}' WHERE id_professor = {id_professor}"
            ) 

            print("-" * 30)
            print("professor atualizado com sucesso!")
            print("-" * 30)

            conexao.commit()

    except ValueError:
        print("-" * 30)
        print("ERROR: digite as informações de forma válida.")
        print("-" * 30)
        return
    
    except sqlite3.IntegrityError:
        print("-" * 30)
        print("ERROR: Campo obrigatório não preenchido / Dados unicos já existentes")
        print("-" * 30)
        return
    
    except sqlite3.OperationalError:
        print("-" * 30)
        print("ERROR: erro no banco de dados (verefique se esta aberto).")
        print("-" * 30)
        return
    
    except IndexError:
        print("-" * 30)
        print("ERROR: Tentativa de acessar um dado de coluna que não existe.")
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return
    


def deletar_professores():    # Deletar professores já registados no banco de dados.
    try:
        ver_professores()

        print("\n ==== EXCLUIR PROFESSORES ====")

        idx = int(input("qual o ID do professor que deseja excluir?: "))

        cursor.execute(
            f"DELETE FROM professores WHERE id_professor = {idx}"
        )

        print("-" * 30)
        print("professor excluido com sucesso!")
        print("-" * 30)

        conexao.commit()

    except ValueError:
        print("-" * 30)
        print("ERROR: digite as informações de forma válida.")
        print("-" * 30)
        return
    
    except IndexError:
        print("-" * 30)
        print("ERROR: Tentativa de acessar um dado de coluna que não existe.")
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return

def menu():     # Menu de interação com o usário.
    try:
        while True:
            print("\n ==== MENU DO USUÁRIO ====")
            print("1 - Registrar Professores")
            print("2 - Ver Professores Registrados")
            print("3 - Atualizar Informações de Professores")
            print("4 - Deletar Professores Registrados")
            print("5 - sair")

            opcao = int(input("Qual opção vai escolher?: "))

            if opcao == 1: registrar_professores()
            elif opcao == 2: ver_professores()
            elif opcao == 3: atualizar_professores()
            elif opcao == 4: deletar_professores()
            elif opcao == 5:
                print("-" * 30)
                print("encerrando sistema...")
                print("-" * 30)
                conexao.close()
                break
            
            else:
                print("-" * 30)
                print("opção invalida! escolha um numero de 1 a 5.")
                print("-" * 30)

    except ValueError:
        print("-" * 30)
        print("ERROR: digite as informações de forma válida.")
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return
    
menu()
