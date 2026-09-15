# Implemente uma busca sequencial que encontre um número em um vetor de 10 posições e retorne seu índice.

numeros = list(range(1, 11))
contador = 0
numero_desejado = int(input("escolha um número de 0 a 10: "))

for numero in numeros:
    if numero == numero_desejado:
        print(f"Número encontrado! O índice dele é: {contador}.")
        break
    else:
        contador += 1