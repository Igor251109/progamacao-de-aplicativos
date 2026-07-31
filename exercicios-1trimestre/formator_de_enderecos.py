# Padronizar como os endereços são impressos em etiquetas de envio.

def gerar_etiqueta(rua, numero, bairro, cidade, cep):
    return f"o endereço é: cep: {cep}, cidade: {cidade}, bairro: {bairro}, rua: {rua} e numero: {numero}."   #organizar e falar o endereço completo.

print("-" * 50)
rua = input("qual o nome da rua?: ")   # rua do desino.

print("-" * 50)
numero = int(input("qual o numero da casa?: "))    #numero do destino.

print("-" * 50)
bairro = input("qual o bairro?: ")   #bairro do destino.

print("-" * 50)
cidade = input("qual a cidade?: ")   #cidade do destino.

print("-" * 50)
cep = int(input("qual o CEP?: "))    # CEP do destino.
print("-" * 50)

etiqueta_gerada = gerar_etiqueta(rua, numero, bairro, cidade, cep)
print(etiqueta_gerada)
print("-" * 50)