def avaliar_desempenho(nota):     #função notas
    if nota >= 9:
        return "Excelente!"
    elif nota >= 7 and nota < 9:
        return"bom"
    elif nota  > 5 and nota < 7:
        return "regular"
    else:
        return "insuficiente"

nota = int(input("qual é a sua nota?: "))
nota_final = avaliar_desempenho(nota)
print(nota_final)