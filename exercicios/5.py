# Faça uma busca sequencial que retorne a primeira e a última posição de um número repetido em um vetor.

posicao = 0
primeiro = -1
ultimo = -1
procurado = 1

lista = [1, 89, 76, 0, 87, 1]
for numero in lista:
    if numero == procurado:
        if primeiro == -1:
            primeiro = posicao
        
        ultimo = posicao
    
    posicao += 1

print(f"a primeira vez que o numero 1 apareceu foi no indice {primeiro}, a segunda foi no indice {ultimo}.")