def eh_par(numero):            #vereficar se o número é par.
    if numero % 2 == 0:
        return "esse numero é par."
    else:
        return "esse numero é impar."

print("-" * 40)
numero = int(input("fale um numero inteiro: "))
print("-" * 40)
vereficacao = eh_par(numero)
print(vereficacao)
print("-" * 40)