id = int(input("qual o seu id?: "))
valor = float(input("qual o valor da compra?: "))

if valor > 500.00 and id % 16:
    print(f"parabéns, usuário {id}! Você ganhou um cupom para sua compra de R$ {valor}")
else:
    print(f"obrigado pela compra, usuário {id}. Continue acompanhando nossas promoções.")
