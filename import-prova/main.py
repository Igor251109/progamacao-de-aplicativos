import sqlite3
from franquias import criar_tabela_franquia, adicionar_franquias, ver_franquias
from clinicas import criar_tabela_clinica, adicionar_clinicas, ver_clinicas, atualizar, deletar

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
            tratar_erros_funcoes(ver_franquias)
            tratar_erros_funcoes(ver_clinicas)

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

tratar_erros_funcoes(criar_tabela_franquia)
tratar_erros_funcoes(criar_tabela_clinica)
tratar_erros_funcoes(menu)