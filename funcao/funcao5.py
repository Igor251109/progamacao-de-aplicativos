def sofrer_dano(dano, vida):
    while vida > 0:
        if dano > vida:
            return "game over, ataque critico!"
        elif dano <= vida:
            vida = vida - dano
            print(f"vida restante: {vida}")
            if vida > 0:
                dano = int(input("qual o dano sofrido pelo monstro?: "))
    if vida == 0:
        return "game over"

vida = 100
dano_sofrido = int(input("qual o dano sofrido pelo monstro?: "))
dano_total = sofrer_dano(dano_sofrido, vida)
print(dano_total)