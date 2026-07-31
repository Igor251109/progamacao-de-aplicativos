comprimento = input("o comprimento está entre 10cm e 12 cm?: ")

if comprimento == "sim":
    print("aprovado")
    largura = input("a largura está entre 5cm e 6cm?: ")
    if largura == "sim":
        print("peça aprovada.")
else:
    print("reprovado. problema no comprimento.")

