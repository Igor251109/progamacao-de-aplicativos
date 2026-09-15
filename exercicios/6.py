# Implemente busca binária em um vetor ordenado de números inteiros. A função deve retornar o índice do elemento ou -1 caso não exista.

def busca_binaria(vetor, procurado):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if procurado == vetor[meio]:
            return f"encontrado! o indice do numero {procurado} é: {meio}"
        
        elif vetor[meio] < procurado:
            inicio = meio + 1

        elif vetor[meio] > procurado:
            fim = meio - 1
        
    return -1


lista = list(range(1, 151))
numero = int(input("digite um numero entre 1 e 150: "))

print(busca_binaria(lista, numero))
