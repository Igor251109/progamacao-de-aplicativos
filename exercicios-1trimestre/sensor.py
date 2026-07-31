temperatura = float(input("qual a temperatuta atual?: "))

if temperatura >= 80:
    print("Perigo! desligando servidor por superaquecimento.")

if temperatura >= 50:
    print("atenção! ventoinhas ligadas ao maximo." )

if temperatura < 50:
    print("temperatura estavel. sistema rodando tranquilamente.")