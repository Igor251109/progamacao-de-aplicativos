from banco import criar_alunos, criar_escolas, criar_turmas
from escola import cadastrar_escolas, listar_escolas
from turmas import cadastrar_turmas, listar_turmas
from alunos import cadastrar_alunos, listar_alunos
import sqlite3

def tratar_erros_funcoes(funcao):
    try:
        return funcao()
    except ValueError as e:
        print("\n dados inválidos", e)
        return
    except sqlite3.OperationalError as e:
        print("\n erro operacional no banco de dados:", e)
        return
    except sqlite3.IntegrityError as e:
        print("\n erro d integridade no banco de dados:", e)
        return
    except KeyboardInterrupt:
        print("\n programa encerrado pelo usuério.")
        return


def menu():
    while True:

        print("1. CADASTRAR ESCOLAS")
        print("2. CADASTRAR TURMAS")
        print("3. CADASTRAR ALUNOS")
        print("4. LISTAR ESCOLAS")
        print("5. LISTAR TURMAS")
        print("6. LISTAR ALUNOS")
        print("7. SAIR ")

        opcao = int(input("qual opção vai escolher?: "))

        if opcao == 1:
            tratar_erros_funcoes(cadastrar_escolas)
            adicionar_turmas = input("deseja adicionar uma turma?: ").strip()

            if adicionar_turmas == "sim" or adicionar_turmas == "s" or adicionar_turmas == "SIM":
                tratar_erros_funcoes(cadastrar_turmas)
                adicionar_aluno = input("deseja adicionar um aluno a uma turma?: ").strip()

                if adicionar_aluno == "sim" or adicionar_aluno == "s" or adicionar_aluno == "SIM":
                    tratar_erros_funcoes(cadastrar_alunos)
        
        elif opcao == 2:
            tratar_erros_funcoes(cadastrar_turmas)
            adicionar_aluno = input("deseja adicionar um aluno a uma turma?: ").strip()
            
            if adicionar_aluno == "sim" or adicionar_aluno == "s" or adicionar_aluno == "SIM":
                tratar_erros_funcoes(cadastrar_alunos)
        
        elif opcao == 3:
            tratar_erros_funcoes(cadastrar_alunos)
        elif opcao == 4:
            tratar_erros_funcoes(listar_escolas)
        elif opcao == 5:
            tratar_erros_funcoes(listar_turmas)
        elif opcao == 6:
            tratar_erros_funcoes(listar_alunos)
        elif opcao == 7:
            break
        else:
            print("\n opção inválida. tente novamente.")
            continue

tratar_erros_funcoes(criar_escolas)
tratar_erros_funcoes(criar_turmas)
tratar_erros_funcoes(criar_alunos)

assert tratar_erros_funcoes(cadastrar_escolas) == "certo"
assert tratar_erros_funcoes(listar_escolas) == "certo"
assert tratar_erros_funcoes(cadastrar_turmas) == "certo"
assert tratar_erros_funcoes(listar_turmas) == "certo"
assert tratar_erros_funcoes(cadastrar_alunos) == "certo"
assert tratar_erros_funcoes(listar_alunos) == "certo"

print("Testes passaram!")

tratar_erros_funcoes(menu)
