# Usando busca sequencial, encontre o maior número de um vetor e informe sua posição.

lista = [0, 90, 189, 9, 6, 70, 35, 87, 21]
maior = lista[0]
procurar = 0

for numero in lista:
    if numero > maior:
        maior = numero
        procurar += 1

print(f"O maior número do vetor é: {maior}; O índice dele é: {procurar}.")