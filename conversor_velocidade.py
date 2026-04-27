def conversor_km_para_ms(km, metros, ms):
    metros = 3.6
    ms = km * metros
    if km >= 80:
        return f"reduza a velocidade! {km}/h equivale a {ms}/s!"
    else:
        return "velocidade dentro do padrão."

metros = 3.6
velocidade = int(input("qual a sua velocidade atual?: "))
conversao = conversor_km_para_ms(velocidade, metros, ms)
print(conversao)