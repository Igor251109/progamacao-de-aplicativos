# Um gerente quer saber a média de vendas de um vendedor e se ele atingiu a meta.


def analisar_vendas(nome, lista_vendas, meta_mensal):   # nome do vendedor, a média de vendas e se ele bateu a meta de vendas ou não.
    media = len(lista_vendas) / 4
    if media >= meta_mensal:
        return f"o vendedor {nome}, teve média de {media} e bateu a meta."
    else:
        return f"o vendedor {nome}, teve média de {media} e não bateu a meta."

nome = "Carlos"   # nome do vendedor.
lista_vendas = [1200, 1500, 1100, 1900]   # lista dos valores das vendas 
meta = 1400   #meta de vendas

vendas_analisadas = analisar_vendas(nome, lista_vendas, meta)
print(vendas_analisadas)