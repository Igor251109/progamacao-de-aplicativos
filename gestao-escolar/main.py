from banco import criar_alunos, criar_escolas, criar_turmas
from escola import cadastrar_escolas, listar_escolas
from turmas import cadastrar_turmas, listar_turmas
from alunos import cadastrar_alunos, listar_alunos
from tratar_erros import tratar_erros_funcoes

def menu():
    while True:
        try:
            print("1. CADASTRAR ESCOLAS")
            print("2. CADASTRAR TURMAS")
            print("3. CADASTRAR ALUNOS")
            print("4. LISTAR ESCOLAS")
            print("5. LISTAR TURMAS")
            print("6. LISTAR ALUNOS")
            print("7. SAIR ")

            opcao = int(input("qual opção vai escolher?: "))

            match opcao:
                case 1:
                    tratar_erros_funcoes(cadastrar_escolas)
                case 2:
                    tratar_erros_funcoes(cadastrar_turmas)
                case 3:
                    tratar_erros_funcoes(cadastrar_alunos)
                case 4:
                    tratar_erros_funcoes(listar_escolas)
                case 5:
                    tratar_erros_funcoes(listar_turmas)
                case 6:
                    tratar_erros_funcoes(listar_alunos)
                case 7:
                    print("programa encerrado.")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
                    continue
                
        except ValueError:
            print("dados inválidos. Tente novamente.")
            continue

tratar_erros_funcoes(criar_escolas)
tratar_erros_funcoes(criar_turmas)
tratar_erros_funcoes(criar_alunos)
tratar_erros_funcoes(menu)

assert tratar_erros_funcoes(cadastrar_escolas) == "certo"
assert tratar_erros_funcoes(listar_escolas) == "certo"
assert tratar_erros_funcoes(cadastrar_turmas) == "certo"
assert tratar_erros_funcoes(listar_turmas) == "certo"
assert tratar_erros_funcoes(cadastrar_alunos) == "certo"
assert tratar_erros_funcoes(listar_alunos) == "certo"

print("Testes passaram!")