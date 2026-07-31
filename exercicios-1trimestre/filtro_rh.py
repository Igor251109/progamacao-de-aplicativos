#Um RH precisa filtrar candidatos por nota técnica e tempo de experiência.

def vereficar_aprovacao(nota_teste, anos_xp,possui_certificacao):   #filtrar candidatos

    if nota_teste >= 80 and anos_xp >= 2 or possui_certificacao == "sim":
        return "contratado!"
    else:
        return "descartar"

print("-" * 45)
nota = float(input("qual a nota você tirou no teste?: "))   # nota tirada pelo candidato

print("-" * 45)
anos = int(input("quantos anos você tem de experiencia?: "))   # anos de experiencia do candidato

print("-" * 45)
certificado = input("tem certificado?: ")   # candidato tem o certificado?
print("-" * 45)

resultado = vereficar_aprovacao(nota, anos, certificado)
print(resultado)
print("-" * 45)