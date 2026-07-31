ataque = int(input("insira o dano do ataque: "))
defesa = int(input("insira a força da defesa: "))

dano = ataque - defesa

if ataque > defesa:
    print("ataque critico! você causou dano no vilão de: ", dano)
if ataque < defesa:
    print("o vilão defendeu o ataque! O dano causado foi: ", dano)