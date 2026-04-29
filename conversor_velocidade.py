def conversor_km_para_ms(velocidade):
    conversao = velocidade / 3.6
    if velocidade > 80:
        return f"reduza a velocidade! ({conversao}m/s.)"
    elif velocidade <= 80:
        return f"velocidade dentro do padrão. ({conversao}m/s.)"

print("-" * 45)
velocidade = int(input("qual a sua velocidade atual?: "))
print("-" * 45)
velocidade_final = conversor_km_para_ms(velocidade)
print(velocidade_final)
print("-" * 45)