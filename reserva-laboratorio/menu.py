import sqlite3
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

        opcao = int(input("Digite a opção que deseja executar: "))

        if opcao == 1: tratarErrosFuncoes(adicionarReservas)
        elif opcao == 2: tratarErrosFuncoes(verReservas)
        elif opcao == 3:
            print("programa encerrado pelo usuário...")
            break
        else:
            print("opção inválida. tente novamente.")
            continue

tratarErrosFuncoes(laboratorios)
tratarErrosFuncoes(menu)