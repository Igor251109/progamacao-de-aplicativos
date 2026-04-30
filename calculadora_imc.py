# Criar uma ferramenta de saúde que recebe múltiplos dados e retorna uma análise completa.

def gerar_relatorio_saude(nome, peso, altura, idade):  # calculo IMC
    imc = altura / peso
    if imc < 18.5:
        return f"O funcionário {nome}, de idade {idade} anos, está abaixo do peso."
    elif imc >= 18.5 and imc <= 24.9:
        return f"O funcionário {nome}, de idade {idade} anos, está dentro do peso normal."
    elif imc > 24.9 and imc <= 29.9:
        return f"O funcionário {nome}, de idade {idade} anos, está acima do peso recomendado."
    elif imc > 29.9:
        return f"O funcionário {nome}, de idade {idade} anos, está obeso."

print("-" * 50)
nome = input("qual seu nome completo?: ")  # nome do funcionário

print("-" * 50)
idade = int(input("qual a sua idade?: "))  #idade do funcionário

print("-" * 50)
peso = float(input("qual o seu peso atual?: "))  # peso do funcionário

print("-" * 50)
altura = float(input("qual a sua altura?: "))  # altura do funcionário
print("-" * 50)

imc_final = gerar_relatorio_saude(nome, peso, altura, idade)
print(imc_final)