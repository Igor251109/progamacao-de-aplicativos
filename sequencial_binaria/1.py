# Exercício 01: O Contador de Passos (Busca Sequencial vs. Binária)
# Objetivo: Medir na prática quantas verificações cada busca realiza.
# Crie uma lista contendo os números ordenados de 1 a 100: numeros = list(range(1, 101)).
# Escreva uma função de Busca Sequencial que procure o número 95 e imprima quantas comparações foram feitas até encontrá-lo.
# Escreva uma função de Busca Binária que procure o mesmo número 95 na mesma lista e imprima a quantidade de comparações realizadas.
# Pergunta de reflexão: Qual foi a diferença na quantidade de comparações entre os dois métodos para achar o mesmo elemento?

numeros = list(range(1, 101))
contador = 0

def busca_sequencial():
    for numero in numeros:
        if numero == 95:
            print("encontrado!")
            print(f"o numero de comparações foram {contador}.")
            break

        else:
            print(f"{numero}, não é 95.")
        
        contador += 1

def busca_binaria():
    inicio = 0
    fim = 99
    busca = 95
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if busca > numeros[meio]:
            inicio = meio + 1

        elif numeros[meio] == busca:
            print(f"Encontrado! {comparacoes} comparações.")
            break

        elif busca < numeros[meio]:
            fim = meio - 1

    else:
        print("Número não encontrado.")


busca_binaria()

resposta = ''' Na busca sequencial, tivemos que fazer muitas comparações para achar o numero. Na Binária, fizemos pouquissimas
comparações para chegar no resultado.'''