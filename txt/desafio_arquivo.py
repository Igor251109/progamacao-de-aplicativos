# Você e seu grupo de amigos decidiram criar uma lista colaborativa de lugares que desejam visitar no futuro.
#Como ninguém quer esquecer as sugestões, você vai desenvolver um programa que funciona como um "Caderno de Viagens" digital,
# onde as ideias ficam salvas mesmo se o computador for desligado.


open('viagens.txt', 'w'). close()

def adicionar_destino():
    nome_cidade = input("qual o nome da próxima cidade?: ")
    print("-" * 70)
    with open('viagens.txt', 'a') as arquivo:
        arquivo.write(nome_cidade + '\n')
    print("cidade adicionada!")

def mostrar_lugares():
    with open('viagens.txt', 'r') as arquivo:
        lugares = arquivo.readlines()

        n = 0
        for lugar in lugares:
            print(f"{n} - {lugar.strip()}")
            n += 1

def atualizar():
    mostrar_lugares()
    print("-" * 70)
    idx = int(input("qual o numero do lugar que deseja atualizar?: "))
    print("-" * 70)
    atualizar = input("qual o nome do lugar?: ")

    with open('viagens.txt', 'r') as arquivo:
        cidades = arquivo.readlines()

    cidades[idx] = atualizar + '\n'
    
    with open('viagens.txt', 'w') as arquivo:
        arquivo.writelines(cidades)
        print("-" * 70)
        print("destino atualizado com sucesso!")

def deletar():
    mostrar_lugares()
    print("-" * 70)
    desistir_destino = int(input("digite o ID do destino que deseja desistir: "))

    with open('viagens.txt', 'r') as arquivo:
        viagens = arquivo.readlines()

    del viagens[desistir_destino]
    print("-" * 70)
    print("destino removido!")

while True:
    print("-" * 70)
    print("1 - adicionar destino/ 2 - mostrar destinos/ 3 - atualizar destinos/ 4 - deletar destino/ 5 - sair")
    print("-" * 70)
    escolha = int(input("qual opção vai escolher?: "))
    print("-" * 70)

    if escolha == 1: adicionar_destino()
    elif escolha == 2: mostrar_lugares()
    elif escolha == 3: atualizar()
    elif escolha == 4: deletar()
    elif escolha == 5:
        print("progama encerrado.")
        print("-" * 70)
        break