# Você quer melhorar sua rotina e decidiu criar um programa para registrar novos hábitos que deseja adotar 
# (como "Beber 2L de água", "Caminhar 30 min", "Ler 10 páginas").
# O programa servirá como um monitor oficial para você não esquecer suas metas.

open('habitos.txt', 'w').close()    # Abrir o arquivo.

def adicionar_habito():   # Adicionar hábito ao arquivo.
    habito = input("qual hábito deseja adicionar no sistema?: ")
    print("-" * 50)

    with open('habitos.txt', 'a') as arquivo:
        arquivo.write(habito + '\n')
        print("hábito adicionado!")

def revisar_mural():      # Ver todos os hábitos exintentes dentro do arquivo.
    with open('habitos.txt', 'r') as arquivo:
        lista = arquivo.readlines()

    n = 0
    for habitos in lista:
        print(f"{n} - {habitos.strip()}")
        n += 1

def atualizar_habitos():     # Atualizar habitos existentes dentro do arquivo.
    revisar_mural()
    print("-" * 50)
    qual_mudar = int(input("qual ID quer mudar?: "))
    print("-" * 50)
    habito_atualizado = input("qual o novo hábito?: ")

    with open('habitos.txt', 'r') as arquivo:
        habitos = arquivo.readlines()

    habitos[qual_mudar] = habito_atualizado + '\n'

    with open('habitos.txt', 'w') as arquivo:
        arquivo.writelines(habitos)
        print("-" * 50)
        print("Hábito atualizado!")

def descartar_habito():       # Excluir um hábito existente dentro do arquivo.
    revisar_mural()
    print("-" * 50)
    idx = int(input("Qual ID quer excluir do sistema?: "))

    with open('habitos.txt', 'r') as arquivo:
        excluir = arquivo.readlines()

    del excluir[idx]
    print("-" * 50)
    print("Hábito excluido do sistema!")

while True:
    print("-" * 50)
    print("1 - Adicionar hábito/ 2 - Ver hábitos/ 3 - Atualizar hábitos/ 4 - Excluir hábito/ 5 - sair")
    print("-" * 50)
    opcoes = int(input("qual opção vai escolher?: "))
    print("-" * 50)

    if opcoes == 1: adicionar_habito()
    elif opcoes == 2: revisar_mural()
    elif opcoes == 3: atualizar_habitos()
    elif opcoes == 4: descartar_habito()
    elif opcoes == 5:
        print("encerrando sistema...")
        print("-" * 50)
        break