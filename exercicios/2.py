# Faça uma busca sequencial que conte quantas vezes um valor aparece em uma lista.

lista = [1, 2, 3, 1 ,50, 89, 654, 32, 1 ,45, 60, 39]
contador = 0
numero_desejado = 1

for numero in lista:
    if numero == numero_desejado:
        contador += 1
print(f"O numero de vezes que o número 1 foi adicionado na lista é: {contador}.")