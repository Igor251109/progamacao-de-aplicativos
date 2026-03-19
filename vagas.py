vaga = int(input("digite o numero de uma vaga de 0 a 3: "))

vagas = ["livre", "ocupado", "livre", "ocupado"]

if vaga % 2 == 0 and vagas == "livre":
    print(f"vaga {vaga} autorizada para estacionar.")
else:
    print(f"vaga {vaga} ocupada.")