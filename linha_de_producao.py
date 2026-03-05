comprimento = input("o comprimento está entre 10cm e 12 cm?: ")

if comprimento == "sim":
    print("comprimento correto: ")
elif comprimento == "não":
    print("Reprovado: Problema no comprimento. ")
else:
    print("reprovado.")

largura = input("a largura está entre 5cm e 6cm?: ")

if largura == "sim":
    print("peça aprovada")
elif largura == "não":
    print("reprovada")
else:
    print("reprovado")