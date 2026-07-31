# Contexto: A secretaria da escola aprovou o banco de dados que o professor criou.
# Agora, sua missão como programador é criar um sistema interativo que converse com o usuário através do terminal,
# colete as informações de um novo aluno e salve tudo dentro do arquivo escola_demonstracao.db
# usando o comando INSERT com F-Strings.

import sqlite3
conexao = sqlite3.connect('escola_demostracao.db')
cursor = conexao.cursor()

   # criar a tabela no banco de dados
cursor.execute ('''CREATE TABLE IF NOT EXISTS alunos (
        id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_aluno TEXT NOT NULL,
        telefone_aluno TEXT NOT NULL,
        turma_aluno TEXT,
        idade_aluno INTEGER NOT NULL,
        cpf_aluno TEXT NOT NULL,
        id_professor_responsavel INTEGER NOT NULL,
        endereco TEXT,
        
        FOREIGN KEY (id_professor_responsavel) REFERENCES professores (id_professor)
    )''')


def registrar_alunos():    # registrar novos alunos no banco de dados.
    print("\n ==== REGISTRAR ALUNO ====")

    try:
        nome = input("qual o nome completo do aluno? (obrigatório): ")
        telefone = input("qual o telefone do aluno? (obrigatório): ")
        turma = input("qual a turma do aluno? (opcional): ")
        idade = int(input("qual a idade do aluno? (obrigatório): "))
        cpf = input("qual o CPF do aluno? (obrigatório): ")
        endereco = input("qual o endereço do aluno? (opcional): ")
        id_prof = int(input("qual o ID do professor responsável? (obrigatório): "))
    

        comando_inserir = f'''insert into alunos (nome_aluno, telefone_aluno, turma_aluno, idade_aluno, cpf_aluno, endereco, id_professor_responsavel)
        values ('{nome}', '{telefone}', '{turma}', {idade}, '{cpf}', '{endereco}', {id_prof})'''

        cursor.execute(comando_inserir)
        conexao.commit()
        
        print("-" * 30)
        print("aluno registrado com sucesso!")
        print("-" * 30)

    except ValueError:
        print("-" * 30)
        print("Erro: digite as informações de forma válida.")
        print("-" * 30)
        return
    
    except sqlite3.IntegrityError:
        # Trata erros causados por violação de regras de integridade, como
        # chaves duplicadas, referências inválidas ou campos obrigatórios.

        # ERROS POSSIVEIS: 
        # VIOLAÇÃO DE PRIMARY KEY
        # A chave primária informada já existe no banco de dados.

        # VIOLAÇÃO DE UNIQUE
        # O valor informado deve ser único, mas já está cadastrado.

        # VIOLAÇÃO DE FOREIGN KEY
        # A referência a outro registro é inválida ou inexistente.

        # VIOLAÇÃO DE NOTNULL
        # Um campo obrigatório não recebeu um valor.

        # VIOLAÇÃO DE CHECK
        # O valor informado não atende às regras definidas para o campo.

        print("-" * 30)
        print("ERROR: Erro de integridade.")
        print("-" * 30)
        return
    
    except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
        print("-" * 30)
        print("Operação cancelada pelo usuário.")
        print("-" * 30)
        return

    


def ver_alunos():      # ver alunos no banco de dados.
    try:
        cursor.execute("SELECT * FROM alunos")
        dados = cursor.fetchall()

        print("\n ==== ALUNOS REGISTRADOS ====")

        for aluno in dados:
            print(f"alunos: {aluno}")
    
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


def atualizar_alunos():      # atualizar alunos no banco de dados
    ver_alunos()

    print("\n ==== ATUALIZAR ALUNOS ====")
    try:
        qual_mudar = int(input("qual ID do aluno que quer atualizar?: "))

        cursor.execute(
            f"SELECT * FROM alunos WHERE id_aluno = {qual_mudar}"
        )

        aluno = cursor.fetchone()

        if not aluno:
            print("-" * 30)
            print("aluno inexintente.")
            print("-" * 30)
            return

        elif aluno:
            novo_nome = input("qual o novo nome do aluno? (obrigatório): ")
            novo_cpf = input("qual é o novo CPF do aluno? (obrigatório): ")
            nova_idade = int(input("qual a nova idade? (obrigatório): "))
            novo_telefone = input("qual o novo telefone? (obrigatório): ")
            nova_turma = input("qual a nova turma do aluno? (opcional): ")
            novo_endereco = input("qual o novo endereço do aluno? (opcional): ")

        cursor.execute(
            f"UPDATE alunos SET nome_aluno = '{novo_nome}', cpf_aluno = '{novo_cpf}', telefone_aluno = '{novo_telefone}', turma_aluno = '{nova_turma}', idade_aluno = {nova_idade}, endereco = '{novo_endereco}' WHERE id_aluno = {qual_mudar}")
        
        print("Aluno atualizado com sucesso!")

        conexao.commit()
    
    except sqlite3.OperationalError:
        #   ERROS POSSIVEIS: 
        # Trata erros operacionais do SQLite, como falha de conexão,
        # tabela inexistente, banco bloqueado ou erro na execução da consulta.

        # AO CONECTAR AO BANCO
        # O banco de dados não pôde ser aberto ou acessado

        # AO EXECUTAR UMA CONSULTA
        # A consulta SQL não pôde ser executada devido a um erro operacional.

        # AO CRIAR TABELAS
        # Ocorreu um erro ao criar ou acessar a estrutura do banco de dados.

        print("-" * 30)
        print("ERROR: erro operacional no banco de dados.")
        print("-" * 30)
        return
    
    except sqlite3.IntegrityError:
        # Trata erros causados por violação de regras de integridade, como
        # chaves duplicadas, referências inválidas ou campos obrigatórios.

        # ERROS POSSIVEIS: 
        # VIOLAÇÃO DE PRIMARY KEY
        # A chave primária informada já existe no banco de dados.

        # VIOLAÇÃO DE UNIQUE
        # O valor informado deve ser único, mas já está cadastrado.

        # VIOLAÇÃO DE FOREIGN KEY
        # A referência a outro registro é inválida ou inexistente.

        # VIOLAÇÃO DE NOTNULL
        # Um campo obrigatório não recebeu um valor.

        # VIOLAÇÃO DE CHECK
        # O valor informado não atende às regras definidas para o campo.

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



def deletar_aluno():       # deletar alunos do banco de dados
    print("\n ==== DELETAR ALUNO ====")
    ver_alunos()

    try:
        qual_deletar = int(input("qual ID do aluno que deseja deletar?: "))

        cursor.execute(
                f"DELETE FROM alunos WHERE id_aluno = {qual_deletar}"
        )
        conexao.commit()
        
        print("aluno removido com sucesso!")
    
    except sqlite3.OperationalError:
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
    op = 0
    while op != 5:
        print("\n ==== MENU DE INTERAÇÃO ====")
        print("1 - adicionar alunos")
        print("2 - ver alunos")
        print("3 - atualizar alunos")
        print("4 - excluir aluno")
        print("5 - sair")
        
        try:
            op = int(input("qual opção vai escolher?: "))

            if op == 1: registrar_alunos()
            elif op == 2: ver_alunos()
            elif op == 3: atualizar_alunos()
            elif op == 4: deletar_aluno()
            elif op == 5:
                print("-" * 30)
                print("encerrando programa...")
                print("-" * 30)
                break
                    
            else:
                print("-" * 30)
                print("Opção invalida. Digite um número de 1 a 5.")
                print("-" * 30)
                continue
        
        except ValueError:
            print("-" * 30)
            print("ERROR: digite um número valido.")
            print("-" * 30)
            continue

        except KeyboardInterrupt:   # quando o usuário está em um input e encerra o terminal, volta para o menu de forma mais bonita.
            print("-" * 30)
            print("Operação cancelada pelo usuário, programa encerrado.")
            print("-" * 30)
            return

menu()
conexao.close()
