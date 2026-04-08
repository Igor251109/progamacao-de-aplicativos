ano = int(input("qual o no que você nasceu?: "))
ano_atual = 2026

menos = ano_atual - ano

if menos >= 18:
    print("você é maior de idade")
else:
    print("você é menor de idade")