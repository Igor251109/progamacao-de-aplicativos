from banco import laboratorios
from reservas import adicionarReservas
from verReservas import verReservas
from tratarErros import tratarErrosFuncoes

def menu():
    while True:
        print("\n ==== MENU DE INTERAÇÃO COM USUÁRIO ====")
        print("1. REALIZAR RESERVAS;")
        print("2. CONSULTAR RESERVAS;")
        print("3. SAIR")
        try:
            opcao = int(input("Digite a opção que deseja executar: "))
            match opcao:
                case 1:
                    adicionarReservas()
                case 2:
                    verReservas()
                case 3:
                    print("saindo...")
                    break
                case _:
                    print("opção inválida. tente novamente.")
                    continue

        except ValueError:
            print("dados inválidos. Tente novamente.")
            continue
        

tratarErrosFuncoes(laboratorios)
tratarErrosFuncoes(menu)