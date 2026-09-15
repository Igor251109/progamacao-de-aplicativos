# Crie uma função de busca sequencial que procure um nome em uma lista de alunos e informe se ele foi encontrado.

def buscar_nomes(nome_procurado, lista_nomes):
    contador = 0
    for nome in lista_nomes:
        if nome == nome_procurado:
            print(f"nome encontrado! O índice dele é {contador}")
            break

        contador += 1

lista = ["igor", "gabriel", "hugo", "vitoria", "julia"]
nome = input("qual nome deseja procurar?: ")

buscar_nomes(nome, lista)